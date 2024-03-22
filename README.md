# PWN_ENV-Helper - 胖環境搭建助手

- Support C, C++ source code.
    - `setup.py` is used to build the file structure.
    - Support Dockerfile and docker-compose.yml to build the PWN environment.

- Compile the source code to binary with `Makefile`, `gcc`.

-  File Structure
    ```
    + src/
    |   |
    |   + chal.c
    |
    + bin/
    |   |
    |   + chal
    |
    + xinetd
    |
    |
    + Docker
        - `Dockerfile`
        - *`docker-compose.yml`
    ```
## Usage

Build the PWN environment with Dockerfile or docker-compose.yml

1. build file structure
    ```bash
    python setup.py -m $machine  -b $bin_name -p $port
    ```
    - `$machine` is the architecture of the binary file.
    - `$bin_name` is the name of the binary file.
    - `$port` is the port number of the service.

2. Put the binary file in the `bin` directory.
    - the name of the binary file should be the same as the `$bin_name`. (name=`$bin_name`)

#### Build with Dockerfile

1. Docker Image Build
    ```bash
    sudo docker build -t "image_name" .
    ```
2. Run the docker container with Docker Image
    ```bash
    docker run -d -p "0.0.0.0:$PUN_PORT:9999" -h "hostname" --name="container_name" image_name
    ```
`$PUN_PORT` is the pubilc port number of the service.

#### Build with docker-compose.yml 

1. Run the docker container with `docker-compose.yml`
    ```bash
    sudo docker-compose up -d
    ```

## Capture traffic

- [TCPDUMP](https://www.tcpdump.org/)
    ```bash
    tcpdump -w demo.pcap -i eth0 port $PUB_PORT
    ```

## References

- [https://github.com/RoderickChan/docker_pwn_env](https://github.com/RoderickChan/docker_pwn_env)