const DEFAULT_LIMIT = 15
const PING_OF_SQUARE_METER = 0.3025

const LEVELS_IN_CH = [
    "零層",
    "一層", "二層", "三層", "四層", "五層", "六層", "七層", "八層", "九層", "十層",
    "十一層", "十二層", "十三層", "十四層", "十五層", "十六層", "十七層", "十八層", "十九層", "二十層",
    "二一層", "二二層", "二三層", "二四層", "二五層", "二六層", "二七層", "二八層", "二九層", "三十層",
    "三一層", "三二層", "三三層", "三四層", "三五層", "三六層", "三七層", "三八層", "三九層", "四十層",
]

const LEVELS_TO_NUMS_MAP = LEVELS_IN_CH
    .map((_, index) => String(index) + "F")
    .reduce((accu, item, index) => {
        return {
            ...accu,
            [LEVELS_IN_CH[index]]: item
        }
    }, {})

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

export {
    DEFAULT_LIMIT,
    LEVELS_TO_NUMS_MAP,

    updateUrl,
    toPing,
    toTenThousand,
    calcUnitPrice,
    generateBuildingArea,
    toDashSymbolIfNoValue,
}