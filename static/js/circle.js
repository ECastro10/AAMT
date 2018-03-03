/**
 * Created by emanuel on 2/7/17.
 */

    var currAngle = 0;

    var ArrayDegrees = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330];

    var degreeSpin = 0;

    var displayAngle = 0;

    function modifyAngle(number){
        return Math.abs(number - 360)
    }


    //The code below is jQuery's rotate function.


    $('#cb').click(function () {

        while (currAngle == degreeSpin){
            degreeSpin = ArrayDegrees[Math.floor(Math.random() * ArrayDegrees.length)];
        }


        $('#circle_image').rotate({

                duration: 2000,

                angle: currAngle,

                animateTo: degreeSpin - 360

            });

        currAngle = degreeSpin;

        displayAngle = (modifyAngle(currAngle));

        //The block below dictates what the display in the key_info shows based on display Angle

        if (displayAngle == 30) {

            $('#current_key').html('G');

            $('#scale_notes').html('G, A, B, C, D, E, F#');

        }
        else if (displayAngle == 60) {

            $('#current_key').html('D');

            $('#scale_notes').html('D, E, F#, G, A, B, C#');

        }
        else if (displayAngle == 90) {

            $('#current_key').html('A');

            $('#scale_notes').html('A, B, C#, D, E, F#, G#');

        }
        else if (displayAngle == 120) {

            $('#current_key').html('E');

            $('#scale_notes').html('E, F#, G#, A, B, C#, D#');

        }
        else if (displayAngle == 150) {

            $('#current_key').html('B');

            $('#scale_notes').html('B, C#, D#, E, F#, G#, A#');

        }
        else if (displayAngle == 180) {

            $('#current_key').html('Gb/F#');

            $('#scale_notes').html('Gb, Ab, Bb, Cb(=B), Db, Eb, F<br/>F#, G#, A#, B, C#, D#, E#(=F)');

        }
        else if (displayAngle == 210) {

            $('#current_key').html('Db/C#');

            $('#scale_notes').html('Db, Eb, F, Gb, Ab, Bb, C<br/>C#, D#, E#(=F), F#, G#, A#, B#(=C)');

        }
        else if (displayAngle == 240) {

            $('#current_key').html('Ab');

            $('#scale_notes').html('Ab, Bb, C, Db, Eb, F, G');

        }
        else if (displayAngle == 270) {

            $('#current_key').html('Eb');

            $('#scale_notes').html('Eb, F, G, Ab, Bb, C, D');

        }
        else if (displayAngle == 300) {

            $('#current_key').html('Bb');

            $('#scale_notes').html('Bb, C, D, Eb, F, G, A');

        }
        else if (displayAngle == 330) {

            $('#current_key').html('F');

            $('#scale_notes').html('F, G, A, Bb, C, D, E');

        }
        else {

            $('#current_key').html('C');

            $('#scale_notes').html('C, D, E, F, G, A, B');

        }


    });


var showNotes = true;

function ShowHideNotes() {

        console.log('In the onclick function');

       if (showNotes == true) {

           console.log(showNotes);
           document.getElementById('scale_notes').style.color = 'black';
           showNotes = false;

       } else if (showNotes == false) {

           console.log(showNotes);
           document.getElementById('scale_notes').style.color = 'white';
           showNotes = true;
       }


}


// var on = false;
//
// function TurnLightOnAndOff() {
//
//
//     if (on == false) {
//         {
//             document.getElementById("lightbulb").style.backgroundColor = "yellow";
//             document.getElementById("text").innerHTML = "<h1>" + "On" + "</h1>";
//             on = true;
//         }
//     }
//     else if (on == true) {
//         document.getElementById("lightbulb").style.backgroundColor = "white";
//         document.getElementById("text").innerHTML = "<h1>" + "Off" + "</h1>";
//         on = false;
//
//     }
// }



