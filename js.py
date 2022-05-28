add_cookies = "Game.cookies += 100;"

clicker = """
    autoClicker = function(clicksAtOnce, repeatInterval) {
        let cheated = false;
        let intoTheAbyss = function() {
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
    clicker = autoClicker(10, 100);
"""

stop_clicker = "clearInterval(clicker);"

buy_bulk = "Game.buyBulk = 10;"

store_items = """
items = {}
Object.keys(Game.Objects).forEach(key => {
    items[key] = Game.Objects[key].amount
});
items;
"""
