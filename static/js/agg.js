var global = 0 // global counting to prevent multi rendering of tables

// compute the content of each table
function grid_options (table_id) {
  const columnDefs = [
    { field: "make" },
    { field: "model" },
    { field: "price" }
  ];
  
  // specify the data
  const rowData = [
    { make: "Toyota", model: table_id, price: 35000 },
    { make: "Ford", model: "Mondeo", price: 32000 },
    { make: "Porsche", model: "Boxster", price: 72000 }
  ];
  
  // let the grid know which columns and what data to use
  const gridOptions = {
    columnDefs: columnDefs,
    rowData: rowData
  };

  return gridOptions
}

// setup the grid after the page has finished loading
document.addEventListener('DOMContentLoaded', () => {
  global += 1; // count the number of time this code is called
  let all_tables = document.querySelectorAll('.agg');

  if (global == all_tables.length) { // run the tables rendering only on the last call
    all_tables.forEach(table => {
      let go = grid_options (table.id)
      new agGrid.Grid(table, go)
    });
  }
});
