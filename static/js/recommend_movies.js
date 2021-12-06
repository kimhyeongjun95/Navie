const startBtn = document.querySelector('.start-btn')
const requestUrl = '/movies/movies_worldcup/'
const firstMovie = document.querySelector('#first-movie')
const secondMovie = document.querySelector('#second-movie')
const tournament = document.querySelector('.tournament')
const vs = document.querySelector('#vs')
let randomMovies = []

function firstSelect () {
  console.log(1)
  console.log(randomMovies)
  if (randomMovies.length === 5) {
    tournament.innerText = '4강'
    console.log(randomMovies.length)
  }

  if (randomMovies.length === 3) {
    tournament.innerText = '결승'
    console.log(randomMovies.length)
  }

  if (randomMovies.length === 2) {
    console.log('한번 더?')
    console.log(randomMovies)
    location.href = `/movies/${randomMovies[0][0]}/${randomMovies[1][0]}/result_recommend/`
  }
  randomMovies.push(randomMovies[0])
  randomMovies.shift()
  randomMovies.shift()
  firstMovie.setAttribute("src", `https://image.tmdb.org/t/p/original${randomMovies[0][1]}`)
  secondMovie.setAttribute("src", `https://image.tmdb.org/t/p/original${randomMovies[1][1]}`)
}
      
function secondSelect() {
  console.log(2)
  console.log(randomMovies)
  if (randomMovies.length === 5) {
    console.log(randomMovies.length)
    tournament.innerText = '4강'
  }

  if (randomMovies.length === 3) {
    tournament.innerText = '결승'
    console.log(randomMovies.length)
  }
  
  if (randomMovies.length === 2) {
    console.log('한번 더?')
    console.log(randomMovies)
    location.href = `/movies/${randomMovies[0][0]}/${randomMovies[1][0]}/result_recommend/`
  }
  randomMovies.push(randomMovies[1])
  randomMovies.shift()
  randomMovies.shift()
  firstMovie.setAttribute("src", `https://image.tmdb.org/t/p/original${randomMovies[0][1]}`)
  secondMovie.setAttribute("src", `https://image.tmdb.org/t/p/original${randomMovies[1][1]}`)
}

startBtn.addEventListener('click', (e) => {
  axios.get(requestUrl)
    .then((res) => {
      randomMovies = res.data.random_movies
      console.log(randomMovies)
      
      tournament.innerText = '8강'
      vs.innerText = 'VS'
      firstMovie.setAttribute("src", `https://image.tmdb.org/t/p/original${randomMovies[0][1]}`)
      secondMovie.setAttribute("src", `https://image.tmdb.org/t/p/original${randomMovies[1][1]}`)
      startBtn.setAttribute("style", "display: none;")

      firstMovie.addEventListener('click', firstSelect)
      secondMovie.addEventListener('click', secondSelect)
    })
})