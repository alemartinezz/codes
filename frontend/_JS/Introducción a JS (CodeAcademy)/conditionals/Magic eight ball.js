const userName = '';
userName ? console.log(`Hello, ${userName}`) : console.log('Hello!');

let userQuestion = 'What you mean i cannot fly?';
console.log(`User ${userName} asked : ${userQuestion}`);

let randomNumber = Math.floor(Math.random() * 7);
let eightBall = '';

switch (randomNumber){
  case 0:
    eightBall = 'It is certain';
    break;
  case 1:
    eightBall = 'It is decidedly so';
    break;
  case 2:
    eightBall = 'Cannot predict now';
    break;
  case 3:
    eightBall = 'Don\'t count on it';
    break;
  case 4:
    eightBall = 'My sources say no';
    break;
  case 5:
    eightBall = 'Outlook not so good';
    break;
  case 6:
    eightBall = 'Signs point to yes';
    break;
  case 7:
    eightBall = 'You are in grave danger';
    break;
  default:
    eightBall = 'Reply hazy try again';
   break;
 }

console.log(`${eightBall}`);

/*
// Output:
Hello!
User  asked : What you mean i cannot fly?
My sources say no
*/
