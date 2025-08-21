# STAGE 1: Build with caching
FROM golang:1.21-alpine AS builder

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

COPY main.go ./
RUN CGO_ENABLED=0 GOOS=linux go build -o backend .

# STAGE 2: Lightweight runtime
FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/

COPY --from=builder /app/backend .
EXPOSE 8080

CMD ["./backend"]
