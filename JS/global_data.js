function getGlobalData() {
    return axios.get("https://corona.lmao.ninja/all");
  }

axios.all(getGlobalData()).then(
axios.spread(function (global) {
    //global
    console.log("Global", "color: #fb5e53");
    console.log("Cases", global.data.cases);
    console.log("Deaths", global.data.deaths);
    console.log("Recovered", global.data.recovered);

    var totalCases = global.data.cases.toLocaleString();
    var totalDeaths = global.data.deaths.toLocaleString();
    var totalRecovered = global.data.recovered.toLocaleString();

    document.getElementsByClassName("global__cases")[0].childNodes[1].innerHTML = totalCases;
    document.getElementsByClassName("global__recovered")[0].childNodes[1].innerHTML = totalRecovered;
    document.getElementsByClassName("global__deaths")[0].childNodes[1].innerHTML = totalDeaths;

    //countries
}));