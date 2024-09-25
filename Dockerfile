FROM python:3.11 as builder

WORKDIR /app/portfolio

ARG DEBIAN_FRONTEND=noninteractive
ARG OUTPUT_DIR=/output

RUN apt update && apt install -y gcc libpython3.11-dev curl patchelf
RUN curl https://get.wasmer.io -sSfL | sh

RUN pip install py2wasm
RUN py2wasm 2>&1 > /dev/null || echo "py2wasm is ready"

COPY . .
RUN apt install -y git && git init
RUN pip install .

RUN mkdir -p "$OUTPUT_DIR"
RUN py2wasm $(which me) --output "$OUTPUT_DIR/me.wasm"
