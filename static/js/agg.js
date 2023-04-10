var global = 0 // global counting to prevent multi rendering of tables

// setup the grid after the page has finished loading
document.addEventListener('DOMContentLoaded', () => {
  global += 1; // count the number of time this code is called
  let all_tables = document.querySelectorAll('.agg');
  
  if (global == all_tables.length) { // run the tables rendering only on the last call
    all_tables.forEach(table => {
      fetch('./'+table.id+'.json')
      .then((response) => response.json())
      .then((json) => {
        new agGrid.Grid(table, json)
      });
    })
  }
})
