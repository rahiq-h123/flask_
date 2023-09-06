document.getElementById('uploadForm').addEventListener('submit', function(e) {
  e.preventDefault(); // Prevent form submission

  var file = document.getElementById('csvFile').files[0]; // Get the selected file

  var reader = new FileReader();
  reader.onload = function(e) {
    var contents = e.target.result; // Get the file contents

    // Send the file contents to the Flask server using AJAX
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var feature = JSON.parse(xhr.responseText).feature; // Extracted feature from the response
        console.log(feature);
      }
    };
    xhr.send(JSON.stringify({ contents: contents }));
  };

  reader.readAsText(file); // Read the file as text
});