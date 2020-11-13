const HTMLSelectors = {
    toggleDiv: () => document.getElementById('toggle-div'),
    allOddsButtons: () => document.getElementsByClassName('odds_column'),
    homeOdd: () => document.getElementById('home_odd'),
    drawOdd: () => document.getElementById('draw_odd'),
    awayOdd: () => document.getElementById('away_odd'),
    betsAppended: () => document.getElementById('games-appended'),
}
for (odd of HTMLSelectors.allOddsButtons()) {
    odd.addEventListener('click', addToCoupon)
}


function addToCoupon(e) {
    e.preventDefault()
    HTMLSelectors.toggleDiv().style.display = 'inline-block';
    console.log(e.target.parentElement.className)
    createMyBetField(e.target.parentElement.parentElement, e.target.parentElement.className, e.target.innerText)
}

function createMyBetField(game, my_bet, my_odd) {
    let myBets = {home_odd: '1', draw_odd: 'X', away_odd: '2'};
    let [time, home_team, away_team, home_odd, draw_odd, away_odd] = game.getElementsByTagName('td');
    console.log(`${home_team.innerText} - ${away_team.innerText} - ${home_odd.innerText} ${draw_odd.innerText} ${away_odd.innerText}`)
    let myBetDiv = document.createElement('div');
    myBetDiv.className = 'my-bet-div';
    let home_team_par = document.createElement('p');
    let away_team_par = document.createElement('p');
    let sign_and_odd_div = document.createElement('div');
    sign_and_odd_div.className = 'sign-and-odd-div';
    let sign_par = document.createElement('p');
    let odd_par = document.createElement('p');

    home_team_par.innerText = home_team.innerText;
    away_team_par.innerText = away_team.innerText;
    sign_par.innerText = myBets[my_bet];
    odd_par.innerText = my_odd;

    sign_and_odd_div.appendChild(sign_par);
    sign_and_odd_div.appendChild(odd_par);
    myBetDiv.appendChild(home_team_par);
    myBetDiv.appendChild(away_team_par);
    myBetDiv.appendChild(sign_and_odd_div);

    HTMLSelectors.betsAppended().appendChild(myBetDiv)
}
