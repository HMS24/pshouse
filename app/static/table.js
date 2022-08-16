const PING_OF_SQUARE_METER = 0.3025

const updateUrl = (prev, query) => {
    return prev + (prev.indexOf("?") >= 0 ? "&" : "?") + new URLSearchParams(query).toString()
}

const toTenThousand = val => String(val / 10000).padEnd(5) + " 萬"
const toPing = val => (val * PING_OF_SQUARE_METER).toFixed(2) + " 坪"

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

// 可以排序的欄位: transaction_date, price and unit_price
const displayColumns = [
    { id: "transaction_date", name: "交易日期" },
    { id: "build_name", name: "建案名稱", sort: false },
    { id: "buildings", name: "建築物", sort: false },
    { id: "level", name: "樓層", sort: false },

    { id: "building_total_area", name: "總坪數", sort: false, formatter: toPing },
    { id: "price", name: "總價", formatter: toTenThousand },
    { id: "unit_price", name: "單價(萬/坪)", formatter: calcUnitPrice },
    { id: "building_area", name: "房屋坪", sort: false, formatter: generateBuildingArea },
    { id: "parking_sapce_price", name: "車位價", sort: false, formatter: toTenThousand },
    { id: "parking_sapce_type", name: "車位類型", sort: false },
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
