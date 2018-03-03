/**
 * Created by emanuel on 3/29/17.
 */

var A4 = 440;
var note_context = new AudioContext();
var note_node = note_context.createOscillator();
var gain_node = note_context.createGain();
note_node.type = 'square';
note_node.frequency.value = 2500;
gain_node.gain.value = 0;
note_node.connect(gain_node);
gain_node.connect(note_context.destination);
note_node.start();
var playing = false;
function toggle_playing_sound() {
    if (playing == false) {
        gain_node.gain.value = 0.1;
        playing = true;
    } else {
        gain_node.gain.value = 0;
        playing = false;
    }
}