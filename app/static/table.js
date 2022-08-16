const updateUrl = (prev, query) => {
    return prev + (prev.indexOf("?") >= 0 ? "&" : "?") + new URLSearchParams(query).toString()
}

const displayColumns = [
    // { id: "id", name: "編號", sort: false },
    { id: "city", name: "城市", sort: false },
    { id: "district", name: "區域", sort: false },
    { id: "build_name", name: "建案名稱", sort: false },
    { id: "object_of_transaction", name: "交易標的", sort: false },
    // { id: "location", name: "位置", sort: false },
    { id: "transaction_date", name: "交易日期", sort: false },
    { id: "building_total_area", name: "總坪數", sort: false },
    { id: "room", name: "房間數", sort: false },
    { id: "restaurant_and_living_room", name: "客餐廳數", sort: false },
    { id: "bathroom", name: "衛浴數", sort: false },
    { id: "buildings", name: "建築物", sort: false },
    { id: "price", name: "總價" },
    { id: "unit_price", name: "單價" },
    { id: "parking_sapce_price", name: "車位價", sort: false },
    // { id: "note", name: "備註", sort: false },
    // { id: "created_at", name: "新增時間", sort: false },
    // { id: "updated_at", name: "更新時間", sort: false },
]

const grid = new gridjs.Grid({
    columns: displayColumns,
    server: {
        url: "/apiv1/deals",
        then: results => results.result.data,
        total: results => results.result.total,
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
        multiColumn: true,
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