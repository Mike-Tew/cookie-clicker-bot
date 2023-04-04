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
        clicker = autoClicker(10, 100);
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
    for (var i in Game.UpgradesInStore) {
        upg = Game.UpgradesInStore[i];
        if (!upg.isVaulted() && upg.pool != 'toggle' && upg.pool != 'tech') {
            upg.buy(1);
        }
    }
"""

click_golden = """
    for (shimmer in Game.shimmers) {
        Game.shimmers[shimmer].pop()
    };
"""

click_ticker = """
    if (Game.TickerEffect.type === 'fortune') {
        Game.tickerL.click()
    }
"""

pop_wrinkler = """
    for (i in Game.wrinklers) {
        if (Game.wrinklers[i].close === 1) {
            Game.wrinklers[i].hp = 0
        }
    }
"""

spell_combo_old = """
    if ('Click frenzy' in Game.buffs || 'Dragonflight' in Game.buffs) {
        for (let i = 0; i < 200; i++) {
            Game.Objects['Mine'].sell(500);
            Game.Objects['Mine'].buy(500);
        }

        spells = Game.Objects['Wizard tower'].minigame
        if (spells.magic === spells.magicM) {
            grimoireSpell1.click()
        }
    }
"""

spell_combo = """
    if (Game.Objects['Wizard tower'].minigame.magic > 99) {
        if (Object.keys(Game.buffs).length > 1) {
            grimoireSpell1.click()
            Game.Objects['Wizard tower'].sell(490)
            setTimeout(() => {
                grimoireSpell1.click()
                Game.storeBulkButton(0)
                Game.Objects['Wizard tower'].buy(490)
            }, 100)
        }
    }
"""

buy_and_sell = """
    if (Object.keys(Game.buffs).length > 2) {
        for (let i = 0; i < 50; i++) {
            Game.Objects['Mine'].sell(800)
            Game.storeBulkButton(0)
            Game.Objects['Mine'].buy(800)
        }
    }
"""
