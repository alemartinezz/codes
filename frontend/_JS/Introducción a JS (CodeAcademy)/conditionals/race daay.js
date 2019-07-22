var signedEarly = false;
let runnersAge = prompt ('Ingrese edad');
let raceNumber = Math.floor(Math.random()*1000);

if (signedEarly === false){
    raceNumber += 1000;
}

if(runnersAge > 18 && signedEarly === true){
    console.log(`you will race at 9:30 am with the number ${raceNumber}`);
    
    } else if(signedEarly === true|| runnersAge > 18){
        console.log(`you will race at 11 pm with the number ${raceNumber}`);

    } else if(signedEarly === false && runnersAge <= 18) {
        console.log(`you will race at 12.30 pm with the number ${raceNumber}`);

    } else {
        console.log('please see registration desk')
}