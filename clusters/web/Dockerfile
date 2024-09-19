FROM rust:slim-bullseye

RUN apt-get --yes update && apt-get --yes install git pkg-config libssl-dev
RUN cargo install trunk
RUN rustup target add wasm32-unknown-unknown
RUN rustup component add rustfmt
RUN rustup component add clippy-preview

WORKDIR /app
COPY . /app

EXPOSE 8000
