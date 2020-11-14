const HTMLSelectors = {
    toggleDiv: () => document.getElementById('toggle-div'),
    allOddsButtons: () => document.getElementsByClassName('odds_column'),
    homeOdd: () => document.getElementById('home_odd'),
    drawOdd: () => document.getElementById('draw_odd'),
    awayOdd: () => document.getElementById('away_odd'),
    betsAppended: () => document.getElementById('games-appended'),
    deleteGamesButton: () => document.getElementById('delete-coupon'),
    totalOddsField: () => document.getElementById('total_odds_field'),
    homeTeamsInCoupon: () => document.getElementsByClassName('home-team-in-coupon'),
    currOddToTakeOut: () => document.getElementById('odd-coupon-par'),
    enterStakeField: () => document.getElementById('enter-stake-field'),
    totalProfitPar: () => document.getElementById('total_profit'),
    toggleStakeProfit: () => document.getElementById('toggle-stake-and-profit'),


}
for (odd of HTMLSelectors.allOddsButtons()) {
    odd.addEventListener('click', addToCoupon)
}

HTMLSelectors.deleteGamesButton().addEventListener('click', cleanCoupon)

HTMLSelectors.enterStakeField().addEventListener('input', updateTotalOdds)

function addToCoupon(e) {
    e.preventDefault()
    let state = checkIfInCoupon(e);
    if (state === 'notinside') {
        HTMLSelectors.toggleDiv().style.display = 'inline-block';
        HTMLSelectors.toggleStakeProfit().style.display = 'inline-block';
        let odd = e.target.innerText;
        createMyBetField(e.target.parentElement.parentElement, e.target.parentElement.className, odd)
        calculateTotalOdds(odd)
    }
}

function cleanCoupon(e) {
    e.preventDefault()
    HTMLSelectors.betsAppended().innerHTML = '';
    HTMLSelectors.toggleDiv().style.display = 'none';
    HTMLSelectors.toggleStakeProfit().style.display = 'none';
    HTMLSelectors.totalOddsField().value = '';
}

function calculateTotalOdds(odd) {
    totalOddsField = HTMLSelectors.totalOddsField()
    if (totalOddsField.value !== ''){
        totalOddsField.value = (totalOddsField.value * odd).toFixed(2);
    } else {
        totalOddsField.value = `${(1 * odd).toFixed(2)}`;
    }
}

function checkIfInCoupon(e) {
    let homeTeam = e.target.parentElement.parentElement.getElementsByClassName('teams_regular')[0].innerText;
    let allHomeTeams = HTMLSelectors.homeTeamsInCoupon();
    let state = 'notinside';
    Object.values(allHomeTeams).forEach(function(team) {
        if (team.innerText === homeTeam) {
            return state = 'inside';
        }
    })
    return state;
}

function updateTotalOdds(e) {
    if (Number(e.target.value) > 0) {
        HTMLSelectors.totalProfitPar().value = Number.parseFloat(HTMLSelectors.totalOddsField().value * e.target.value).toFixed(2);
    } else {
        HTMLSelectors.totalProfitPar().value = '';
    }
} 

function createMyBetField(game, my_bet, my_odd) {
    let myBets = {home_odd: '1', draw_odd: 'X', away_odd: '2'};
    let [time, home_team, away_team, home_odd, draw_odd, away_odd] = game.getElementsByTagName('td');
    let myBetDiv = document.createElement('div');
    myBetDiv.className = 'my-bet-div';
    let home_team_par = document.createElement('p');
    home_team_par.className = 'home-team-in-coupon';
    let away_team_par = document.createElement('p');
    let sign_and_odd_div = document.createElement('div');
    sign_and_odd_div.className = 'sign-and-odd-div';
    let sign_par = document.createElement('p');
    let odd_par = document.createElement('p');
    odd_par.id = 'odd-coupon-par'
    let delButt = document.createElement('button');
    delButt.id = 'remove-game-from-coupon-button';
    delButt.textContent = 'X';
    delButt.addEventListener('click', removeGameFromCoupon)

    home_team_par.innerText = home_team.innerText;
    away_team_par.innerText = away_team.innerText;
    sign_par.innerText = myBets[my_bet];
    odd_par.innerText = `${Number.parseFloat(my_odd).toFixed(2)}`;

    sign_and_odd_div.appendChild(sign_par);
    sign_and_odd_div.appendChild(odd_par);
    sign_and_odd_div.appendChild(delButt);
    myBetDiv.appendChild(home_team_par);
    myBetDiv.appendChild(away_team_par);
    myBetDiv.appendChild(sign_and_odd_div);

    HTMLSelectors.betsAppended().appendChild(myBetDiv)
}

function removeGameFromCoupon(e) {
    let odd = e.target.parentElement.getElementsByTagName('p')[1].innerText
    let totalOddsField = HTMLSelectors.totalOddsField()
    totalOddsField.value = `${Number.parseFloat(totalOddsField.value / odd).toFixed(2)}`
    if (totalOddsField.value == '1.00') {
        totalOddsField.value = '';
        HTMLSelectors.toggleDiv().style.display = 'none';
        HTMLSelectors.toggleStakeProfit().style.display = 'none';
    }
    e.target.parentElement.parentElement.remove()
}
