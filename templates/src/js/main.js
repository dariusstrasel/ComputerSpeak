/**
 * Created by dariusstrasel on 4/4/17.
 */
console.log("Success.");

function getTranslation(input_type, inputText, output_type, callback) {
// input_types=TEXT&inputText=test&output_types=OCT
  $.ajax({
    url: "/translate/",
    dataType: "json",
    data: {
      'input_types': input_type,
      'inputText': inputText,
      'output_types': output_type
    },
    success: function(response) {
        mutateFieldState(response.output_text);
    }
  });
}

var buttonAjax = $('#translate')
    .on('click', function selectValues(event){
        event.preventDefault();
        var inputText = document.getElementById('input').value;
        if (inputText === ''){
            return
        }

        var input_type = $("#input_type option:selected").val();
        var output_type = $("#output_type option:selected").val();
        console.log(inputText, input_type, output_type);

        var translation = getTranslation(input_type, inputText, output_type);
        console.log(translation);
        return mutateFieldState(translation);
});

function mutateFieldState(newValue){
    console.log("Mutating...");
    return $('#output_translation').text(newValue);
}
