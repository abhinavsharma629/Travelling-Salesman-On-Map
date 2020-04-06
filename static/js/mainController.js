$(function() {
  $("#profile").click(function() {
    // console.log($("#profile1").html())
    profile();
    if (!$("#profile1").html()) {
      update();
    }
  });

  $("#history").click(function() {
    history();
  });
});
