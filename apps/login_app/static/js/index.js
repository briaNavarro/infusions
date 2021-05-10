// console.log('yo');


// var a = 100;

// var b = 100;

// if (a == b) {
//     console.log('they match')


// } else {
//     console.log('wrong foo')
// }

- var cards = [{ title: 'Mountain View', copy: 'Check out all of these gorgeous mountain trips with beautiful views of, you guessed it, the mountains', button: 'View Trips' }, { title: 'To The Beach', copy: 'Plan your next beach trip with these fabulous destinations', button: 'View Trips' }, { title: 'Desert Destinations', copy: 'It\'s the desert you\'ve always dreamed of', button: 'Book Now' }, { title: 'Explore The Galaxy', copy: 'Seriously, straight up, just blast off into outer space today', button: 'Book Now' }]


mixin card(title, copy, button)
  .card
    .content
      h2.title= title
      p.copy= copy
      button.btn= button

main.page-content
  each card in cards
    +card(card.title, card.copy, card.button)