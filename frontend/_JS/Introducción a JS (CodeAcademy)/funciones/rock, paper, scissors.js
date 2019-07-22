const getUserChoice = (userInput) => {
    userInput = prompt ('Choose: rock, paper, or scissors');
    userInput = userInput.toLowerCase();

    switch (userInput) {
        case 'rock':
            return userInput;
        case 'scissors':
            return userInput;
        case 'paper':
            return userInput;
        default:
            console.log ('That`s not a valid option')
    }
}

function getComputerChoice() {
    let randomNumber = (Math.floor(Math.random() * 3))

    switch (randomNumber) {
    case 0:
        return 'rock';
    case 1:
        return 'paper';
    case 2:
        return 'scissors';
    }
}

function determineWinner (userChoice, computerChoice) {
  if (userChoice === computerChoice) {
    return 'Game is a tie!';
  }
  if (userChoice === 'rock') {
    if (computerChoice === 'scissors') {
      return 'You win!';
    } else {
      return 'The computer wins!'; 
    }
  }
  if (userChoice === 'paper') {
   if (computerChoice === 'scissors') {
     return 'The computer wins!';
   } else {
     return 'You win!';
   }
  }
  if (userChoice === 'scissors') {
    if (computerChoice === 'rock') {
      return 'The computer wins!'
    } else {
      return 'You win!';
    }
  }
}

const playGame = () => {
  const userChoice = getUserChoice();
  const computerChoice = getComputerChoice();

  console.log('You threw: ' + userChoice);
  console.log('Computer threw: ' + computerChoice)
  console.log(determineWinner(userChoice, computerChoice));
}

playGame();