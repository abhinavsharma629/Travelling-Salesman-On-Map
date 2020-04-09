function profile() {
  var points_dict = {};
  var count = 0;

  if ($("#profile1").html()) {
    $("#profile1").attr("style", "display:block;");
    $("#history1").attr("style", "display:none;");
  } else {
    $("#profile1").attr("style", "display:block;");
    $("#history1").attr("style", "display:none;");

    $("#profile1").html(
      `
      <div id="original">
        <div class="row">
          <div style="width:50%;">
            <div id='searchBoxContainer'>
              <input class="form-control" type="text" id='searchBox' placeholder="Search Place">
            </div>
          </div>
          <div style="margin-left:5%;">
            <button class="btn btn-outline-secondary" id="calculate" type="button">Calculate Best Route</button>
          </div>
        </div>

        <div id="myMap" style="position:absolute;margin-top:5px;"></div>
      </div>

    `
    );

    $("#calculate").click(function() {
      console.log(positions_object);
      if (Object.keys(positions_object).length > 1) {
        document.getElementById("points").value = JSON.stringify(
          positions_object
        );
        document.getElementById("ninja").submit();
      } else {
        alert(
          "You must select more than 1 set of points to calculate effective distance between them!!"
        );
      }
    });
  }
}
