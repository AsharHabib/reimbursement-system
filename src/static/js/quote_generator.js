//Big array of 20 quotes
const quotes = ["Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.",
"Wikipedia is the best thing ever. Anyone in the world can write anything they want about any subject. So you know you are getting the best possible information.",
"I saved a life. My own. Am I a hero?… I really can't say, but yes.",
"Do I need to be liked? Absolutely not. I like to be liked. I enjoy being liked. I have to be liked, but it's not like this compulsive need to be liked, like my need to be praised.",
"I love inside jokes. I hope to be a part of one someday.",
"You know what they say 'Fool me once, strike one, but fool me twice… strike three.'",
"I'm not superstitious but I am a little stitious.",
"And I knew exactly what to do. But in a much more real sense, I had no idea what to do.",
"The worst thing about prison was the dementors.",
"Tell him to call me ASAP as possible.",
"When the son of the deposed king of Nigeria emails you directly, asking for help, you help! His father ran the freaking country! OK?",
"I am running away from my responsibilities. And it feels good.",
"It takes you thirty seconds to brush your teeth? Wow, that's ten times as long as it takes me.",
"I've got to make sure that YouTube comes down to tape this.",
"OK, too many different words from coming at me from too many different sentences.",
"My mind is going a mile an hour.",
"It just seems awfully mean. But sometimes, the ends justify the mean.",
"Here it is, heart of New York City, Times Square… named for the good times you have when you're in it.",
"Well, well, well, how the turntables.",
"It's a good thing Russia doesn't exist anymore."]
//Generate random number between 0 - 20
let randomNumber = Math.floor(Math.random() * 20)
//Set the #random-quote h3 tag in index.html to have the quote be it's inner HTML
document.getElementById('random-quote').innerHTML = '\"' + quotes[randomNumber] + '\"' + ''