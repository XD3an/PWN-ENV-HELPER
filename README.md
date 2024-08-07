# PWN-ENV-Helper - 胖環境搭建助手

輔助搭建 PWN 的小工具，支援 Dockerfile 和 docker-compose.yml 來建立 PWN 環境。
- `setup.py`：用來建立檔案結構。
- 支援 Dockerfile 和 docker-compose.yml 來建立 PWN 環境。

-  檔案結構
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

建立 PWN 環境，使用 Dockerfile 或 docker-compose.yml

步驟：
1. 使用 `setup.py` 建立檔案結構
    ```bash
    python setup.py -m $machine  -b $bin_name -p $port
    ```
    - `$machine` 指定機器的架構 (images name, e.g. ubuntu:22.04).
    - `$bin_name` 指定 binary file 的名稱 (binary name).
    - `$port` 指定服務的 port number (service port number in container).

2. 將 binary file 放在 `bin` 目錄下
    - binary file 的名稱應該與 `$bin_name` 相同。 (name=`$bin_name`)

3. 根據 `Dockerfile` 或 `docker-compose.yml` 來建立 PWN 環境，並啟動服務。

#### Build with Dockerfile

1. 建立 Docker image 
    ```bash
    docker build -t "image_name" .
    ```
2. 啟動 Docker container
    ```bash
    docker run -d -p "0.0.0.0:$PUBLIC_PORT:$SERVICE_PORT" -h "hostname" --name="container_name" image_name
    ```

- 警告：在啟動 Docker container 時，請確保以下參數正確：
    - `$SERVICE_PORT` 是 container 內服務的 port number。
    - `$PUBLIC_PORT` 是服務的公開 port number。

#### Build with docker-compose.yml 

1. 啟動 Docker container
    ```bash
    docker-compose up -d
    ```

## Capture traffic

- [TCPDUMP](https://www.tcpdump.org/)
    ```bash
    tcpdump -w demo.pcap -i eth0 port $PUB_PORT
    ```

## References

- [https://github.com/Eadom/ctf_xinetd](https://github.com/Eadom/ctf_xinetd)

- [https://github.com/RoderickChan/docker_pwn_env](https://github.com/RoderickChan/docker_pwn_env)