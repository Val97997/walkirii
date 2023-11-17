$( function() {
    $( "#datepicker" ).datepicker();
    $("#datepicker").datepicker({
      dateFormat: "yyyy-mm-dd"
    })
    $("#datepicker").datepicker({
      dayNamesMin: ["Lu", "Ma", "Mer", "Je", "Ven", "Sa", "Dim"]
    })
    let dayNamesMin = $( "#datepicker" ).datepicker( "option", "dayNamesMin" );
    $( "#datepicker" ).datepicker( "option", "dayNamesMin", [ "Lu", "Ma", "Mer", "Je", "Ven", "Sa", "Dim" ] );

     $( "#datepicker" ).datepicker({
       closeText: "Close"
     })
     $( "#datepicker" ).datepicker({
       showButtonPanel: true
     });
     let showButtonPanel = $( "#datepicker" ).datepicker( "option", "showButtonPanel" );
     $( "#datepicker" ).datepicker( "option", "showButtonPanel", true );
     
 } );
 $(function() {
     $( "#datepicker1" ).datepicker();
    $("#datepicker1").datepicker({
      dateFormat: "yyyy-mm-dd"
    })
    $("#datepicker1").datepicker({
      dayNamesMin1: ["Lu", "Ma", "Mer", "Je", "Ven", "Sa", "Dim"]
    })
    let dayNamesMin = $( "#datepicker1" ).datepicker( "option", "dayNamesMin" );
    $( "#datepicker1" ).datepicker( "option", "dayNamesMin", [ "Lu", "Ma", "Mer", "Je", "Ven", "Sa", "Dim" ] );

     $( "#datepicker1" ).datepicker({
       closeText: "Close"
     })
     $( "#datepicker1" ).datepicker({
       showButtonPanel: true
     });
     let showButtonPanel = $( "#datepicker1" ).datepicker( "option", "showButtonPanel" );
     $( "#datepicker1" ).datepicker( "option", "showButtonPanel", true );
 });
let i = 0;
function timeIncrease() {
  document.getElementById('time').value = ++i;
}
function timeDecrease() {
  if(document.getElementById('time').value > 0){
    document.getElementById('time').value = --i;
  }else if (document.getElementById('time').value<=0){
    window.alert('Value cant be negative')
  }
}