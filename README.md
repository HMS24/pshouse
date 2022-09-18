# pshouse
預售屋實價登錄列表 pre-sale house

## 描述

客製化實價登錄列表，快速瀏覽全貌。鍵入關鍵字能搜尋預售案，也能依照交易日、總價或單價做排序。

正所謂便宜治百病，價格是許多看房優先考慮的因素。尤其是最近成交的幾筆更是與代銷議價的參考。
因此為了簡單化搜尋、排序功能，而快速產生了這個專案。

使用 `Flask` 框架開發 APIs 及 `Grid.js` 實作前端表格。資料由 [pshouse_schedule](https://github.com/HMS24/pshouse_schedule) 專案定期向內政部更新資料到 MySQL 資料庫。

**限制 1: 目前僅擷取新北市全區 2 年內登錄的預售案。首頁預設為新北市淡水區，無法修改區域但可以 [call API](https://github.com/HMS24/pshouse#api-spec) 抓其他區的資料。**

**限制 2: 專案與 [pshouse_schedule](https://github.com/HMS24/pshouse_schedule) 的排程合作，共用 database 並由 web application 負責 migrate database。缺點是得維護兩邊的 model 層並增加一些部署上的困擾🥲**
    
## 如何使用
### 開發

    $ pip3 install -r requirements/common.txt
    $ flask deploy
    $ flask run

### 部署前置作業

要部署到遠端機器，假設目標機器 OS 為 `Ubuntu 20.04`:
1. 安裝 `docker` and `docker compose`
2. 新增資料夾 `mkdir ~/psh` ([`./deploy/publish.sh`](https://github.com/HMS24/pshouse/blob/master/deploy/publish.sh#L17) 有寫入資料夾的名稱 )
3. 設置環境變數 `cd ~/psh && vi .env`
    - `MYSQL_ROOT_PASSWORD` [mariadb container 使用](https://github.com/HMS24/pshouse/blob/master/compose.yml#L12)
    - `MYSQL_DATABASE` [mariadb container 使用](https://github.com/HMS24/pshouse/blob/master/compose.yml#L12)
    - `DATABASE_URI` 預設 sqlite
    - `DATA_REVEAL_DAYS` 資料區間，預設 365 天
    - `TZ` container database 時區，使用 `Asia/Taipei`

### 本地部署
    
設置環境變數

    $ cp .env.example .env

建立映像檔並部署。預設映像檔名稱及版本: `local/psh:latest`。除了 build app 之外還會 build proxy。

    $ ./run.sh --target local

查看 log

    $ docker compose logs -f

### 遠端部署

建立映像檔上傳 docker hub 並部署，預設映像檔名稱:`$DOCKER_USER/$IMAGE:$TAG`。除了 build app 之外還會 build proxy。

    $ ./run.sh --target $REMOTE_MACHINE \
               --ssh-pem $REMOTE_MACHINE_PEM_PATH \
               --docker-user $DOCKER_USER \
               --docker-pass $DOCKER_PASSWORD_PATH \
               --image $IMAGE \
               --tag $TAG \

Parameters
- `REMOTE_MACHINE`: 遠端機器 (user@hostname)
- `REMOTE_MACHINE_PEM_PATH`: pem 檔案位置 ("$HOME/***.pem")
- `DOCKER_USER`: docker 使用者
- `DOCKER_PASSWORD_PATH` docker 密碼檔案位置 ("$HOME/***")
- `IMAGE`(optional): 映像檔名稱
- `TAG`(optional) 映像檔 tag

## 架構

```shell
.
├── build
│   ├── app
│   │   ├── test.sh         # 啟動一個 container 跑測試
│   │   └── Dockerfile
│   ├── proxy
│   │   ├── conf            # nginx conf
│   │   └── Dockerfile
│   ├── build.sh
│   └── push.sh
├── deploy               
│   ├── deploy.sh           
│   └── publish.sh          # 在遠端機器部署的 script
├── migrations              # 紀錄資料庫 schemas 的版本
├── tests                   
├── requirements            
├── app
│   ├── api
│   │   ├── deals.py
│   │   ├── decorators.py
│   │   └── errors.py
│   ├── errors
│   │   └── handlers.py     # 處理 api error response 或 回傳 error html
│   ├── main
│   │   └── views.py        # 前端 route 及 view funcition
│   ├── static           
│   ├── template
│   ├── exceptions.py
│   ├── schemas.py          # serializing and args parse schema
│   ├── models.py
│   ├── stores.py           # 資料庫操作邏輯
│   └── utils.py
├── .env                    
├── pshouse.py              # 程式入口
├── config.py
├── boot.sh                 # container entrypoint script
├── compose.yml
└── run.sh                  # 執行 build and deploy 的 script
```

## API spec
### (deals 實價登錄交易) 相關 endpoints

- [Show deals](https://github.com/HMS24/pshouse/blob/master/assets/api_spec/show_deals.md) : GET /apiv1/deals
- [Show a deal](https://github.com/HMS24/pshouse/blob/master/assets/api_spec/show_deals.md) : GET /apiv1/deals/2

## 預計工作
- 功能
    - 篩選縣市後，列出該縣市區域 tag，點選 tag 可以 get deals by city and district。
- code
    - `schemas.py` 將 serializing 及 args parse 的 schema 拆開，目前放一起。
- 測試
    - get deals 更多 case
    - store crud 的 unit test
