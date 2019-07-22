const lifePhase = () => {
  let age = prompt ('Enter your age in years')

  switch (true){
    case (age <=3 && age >= 0):
      return console.log('baby')
    case (age <=12 && age >= 4):
      return console.log('child')
    case (age <=19 && age >= 13):
      return console.log('teen')
    case (age <=65 && age >= 20):
      return console.log('adult')
    case (age <=140 && age >= 64):
      return console.log('senior citizen')
    case (age >=140):
      return console.log('Immortal')
  }
}
  
lifePhase()