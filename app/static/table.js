const PING_OF_SQUARE_METER = 0.3025

const updateUrl = (prev, query) => {
    return prev + (prev.indexOf("?") >= 0 ? "&" : "?") + new URLSearchParams(query).toString()
}

const toTenThousand = val => val ? String(val / 10000).padEnd(5) + " 萬" : "-"
const toPing = val => val ? (val * PING_OF_SQUARE_METER).toFixed(2) + " 坪" : "-"
const toDashSymbolIfNoValue = val => val ? val : "-"

const generateBuildingArea = (_, row) => {
    const totalArea = row.cells[4].data
    const parkingArea = row.cells[10].data
    const buildingArea = (totalArea - parkingArea) * PING_OF_SQUARE_METER

    return buildingArea.toFixed(2) + " 坪"
}

const calcUnitPrice = (_, row) => {
    const price = row.cells[5].data
    const parkingPrice = row.cells[8].data
    const totalArea = row.cells[4].data
    const parkingArea = row.cells[10].data
    const buildingArea = (totalArea - parkingArea) * PING_OF_SQUARE_METER

    return ((price - parkingPrice) / (buildingArea * 10000)).toFixed(2) + " 萬"
}

const levelsInCh = [
    "零層",
    "一層", "二層", "三層", "四層", "五層", "六層", "七層", "八層", "九層", "十層",
    "十一層", "十二層", "十三層", "十四層", "十五層", "十六層", "十七層", "十八層", "十九層", "二十層",
    "二一層", "二二層", "二三層", "二四層", "二五層", "二六層", "二七層", "二八層", "二九層", "三十層",
    "三一層", "三二層", "三三層", "三四層", "三五層", "三六層", "三七層", "三八層", "三九層", "四十層",
]

const levelsToNumsMap = levelsInCh
    .map((_, index) => String(index) + "F")
    .reduce((accu, item, index) => {
        return {
            ...accu,
            [levelsInCh[index]]: item
        }
    }, {})

// 可以排序的欄位: transaction_date, price and unit_price
const displayColumns = [
    { id: "transaction_date", name: "交易日期" },
    { id: "build_name", name: "建案名稱", sort: false },
    { id: "buildings", name: "建築物", sort: false },
    { id: "level", name: "樓層", sort: false, formatter: val => levelsToNumsMap[val] },

    { id: "building_total_area", name: "總坪數", sort: false, formatter: toPing },
    { id: "price", name: "總價", formatter: toTenThousand },
    { id: "unit_price", name: "單價(萬/坪)", formatter: calcUnitPrice },
    { id: "building_area", name: "房屋坪", sort: false, formatter: generateBuildingArea },
    { id: "parking_sapce_price", name: "車位價", sort: false, formatter: toTenThousand },
    { id: "parking_sapce_type", name: "車位類型", sort: false, formatter: toDashSymbolIfNoValue },
    { id: "parking_sapce_total_area", name: "車位坪", sort: false, formatter: toPing },

    // 以下隱藏
    { id: "city", name: "城市", sort: false, hidden: true },
    { id: "district", name: "區域", sort: false, hidden: true },
    { id: "room", name: "房間數", sort: false, hidden: true },
    { id: "restaurant_and_living_room", name: "客餐廳數", sort: false, hidden: true },
    { id: "bathroom", name: "衛浴數", sort: false, hidden: true },
    { id: "note", name: "備註", sort: false, hidden: true },
]

const grid = new gridjs.Grid({
    columns: displayColumns,
    server: {
        url: "/apiv1/deals",
        then: fetched => fetched.result.data,
        total: fetched => fetched.result.total,
    },
    search: {
        enabled: true,
        server: {
            url: (prev, search) => {
                return updateUrl(prev, { search })
            },
        },
    },
    sort: {
        enabled: true,
        multiColumn: false,
        server: {
            url: (prev, columns) => {
                const columnIndices = displayColumns.map(column => column.id)
                const sort = columns.map(col => (col.direction === 1 ? "+" : "-") + columnIndices[col.index])
                return updateUrl(prev, { sort })
            },
        },
    },
    pagination: {
        enabled: true,
        server: {
            url: (prev, page, limit) => {
                return updateUrl(prev, {
                    start: page * limit,
                    length: limit,
                })
            },
        },
    },
})

grid.render(document.getElementById("table"))
