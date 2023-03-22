add_cookies = "Game.cookies += 100;"

check_page_load = """Game.cookies;"""

clicker = """
    if (typeof clicker === 'undefined') {
        const autoClicker = (clicksAtOnce, repeatInterval) => {
            let cheated = false;
            const intoTheAbyss = () => {
                if(!cheated) {
                    cheated = true;
                    for(let i = 0; i < clicksAtOnce; i++) {
                        Game.ClickCookie();
                        Game.lastClick = 0;
                    }
                    cheated = false;
                };
            };
            return setInterval(intoTheAbyss, repeatInterval);
        };
        clicker = autoClicker(<CLICKS>, 100);
    }
"""

stop_clicker = "clearInterval(clicker); clicker = undefined"

buy_bulk = "Game.buyBulk = 10;"

store_items = """
    items = {};
    Object.keys(Game.Objects).forEach(key => {
        items[key] = Game.Objects[key].amount
    });
    items;
"""

buy_building = """
    Game.storeBulkButton(0);
    building = Game.Objects['<BUILDING>'];
    if (typeof building !== 'undefined') {
        building.buy(1);
    }
"""

buy_upgrade = """
    upgrade = Game.UpgradesInStore[0];
    if (typeof upgrade !== 'undefined') {
        upgrade.buy();
    }
"""
