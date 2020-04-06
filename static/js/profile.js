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
        <div id="myDiv">
        <div class="form-row">

        <div class="form-group col-md-3">
        <label for="long">Longitude</label>
        <input type="number" class="form-control" id="long" placeholder="Longitude">
        </div>
        <div class="form-group col-md-3">
        <label for="lat">Latitude</label>
        <input type="number" class="form-control" id="lat" placeholder="Latitude">
        </div>
        <div class="form-group col-md-2" style="margin-top:30px;">
        <button class="btn11" id="add_point"><i class="fa fa-plus"></i></button>
        </div>
        </div>
        <br>
        <hr>
        <h3>Your Points</h3>
        <br>
        <div id="list">
        </div>


        <br>
        <button type="submit" id="calc_dist" class="btn btn-primary">Calculate Distance</button>

        </div>
    `
    );

    $("#calc_dist").click(function() {
      console.log("calculating dist");
    });

    $("#add_point").click(function() {
      if ($("#long").val().length > 0 && $("#lat").val().length > 0) {
        points_dict[count] = {
          longitude: $("#long").val(),
          latitude: $("#lat").val()
        };

        count += 1;
        $("#list").append(
          `
        <div class="form-row" id="` +
            count +
            `">
        <div class="form-group col-md-3" >
        <label>Longitude</label>
        <input type="number" value="` +
            $("#long").val() +
            `" class="form-control" placeholder="Longitude" disabled>
        </div>
        <div class="form-group col-md-3">
        <label>Latitude</label>
        <input type="number" value="` +
            $("#lat").val() +
            `" class="form-control" placeholder="Latitude" disabled>
        </div>
        <div class="form-group col-md-2" style="margin-top:30px;">
        <button class="btn12 remove_point" id="butt-` +
            count +
            `"><i class="fa fa-minus"></i></button>
        </div>
        <br>
        </div>

        `
        );
        $("#long").val("");
        $("#lat").val("");

        $(".remove_point").click(function() {
          console.log("removing");
          let id = $(this)
            .attr("id")
            .split("-")[1];
          console.log(id);
          $("#" + id).remove();

          delete points_dict[id];
          count -= 1;
          if (count < 0) {
            count = 0;
          }
          console.log(points_dict);
        });
      } else {
        alert("You must provide both Longitude and Latitude");
      }
    });
  }
}
