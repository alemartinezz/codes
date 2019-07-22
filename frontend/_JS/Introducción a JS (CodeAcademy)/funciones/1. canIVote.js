The most common minimum age to vote is 18. Write a function canIVote() that takes in a number, representing the person's age, and returns the boolean true if they are 18 years old or older, and the boolean false if they are not.

// Write your function here:

const canIVote = age => {
    if (age >= 18){
            return true;
        }
    return false;
  } 
  
  canIVote (18);
  
  // Uncomment the line below when you're ready to try out your function
  // console.log(canIVote(19)) // Should print true
  
  // We encourage you to add more function calls of your own to test your code!
  