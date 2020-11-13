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
    console.log(e.target.innerText)
    
}
