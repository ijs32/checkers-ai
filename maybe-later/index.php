<?php 

?>
<html>
    <head>
        <link rel="stylesheet" href="./index.css">

    </head>
    <body>
        <h1>Welcome to Checkers </h1>
        <h3>prepare to get absolutely annihilated by an AI</h3>
        <div id="board-outline">
            <div id="board">

            </div>
        </div>
    </body>
    <script>
        var canvas = document.createElement('canvas');
        canvas.width = canvas.height = 1000;
        var context = canvas.getContext('2d');
        for (var x = 0; x < 8; x++) for (var y = 0; y < 8; y++) {
            context.fillStyle = (x + y) % 2 ? 'white' : 'black';
            context.fillRect(100 * x, 100 * y, 100, 100)
        }
        document.querySelector('#board').appendChild(canvas);
    </script>
</html>