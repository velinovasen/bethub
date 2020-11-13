const HTMLSelectors = {
    allOddsButtons: () => document.getElementsByClassName('odds_column'),
    homeOdd: () => document.getElementById('home_odd'),
    drawOdd: () => document.getElementById('draw_odd'),
    awayOdd: () => document.getElementById('away_odd'),
}
for (odd of HTMLSelectors.allOddsButtons()) {
    odd.addEventListener('click', addToCoupon)
}


function addToCoupon(e) {
    e.preventDefault()
    createMyBetField(e.target.parentElement.parentElement)
}

function createMyBetField(game) {
    let [time, home_team, away_team, home_odd, draw_odd, away_odd] = game.getElementsByTagName('td');
    console.log(`${home_team.innerText} - ${away_team.innerText} - ${home_odd.innerText} ${draw_odd.innerText} ${away_odd.innerText}`)
    let myBetField = document.createElement('input');
    myBetField.disabled = true
}
