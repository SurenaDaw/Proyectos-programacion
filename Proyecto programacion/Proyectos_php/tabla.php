<?php

$juegos = [
    ["persona", "rpg", 2222],
    ["pokemon", "pokemon", 3333],
    ["metaphor", "rpg", 4444],
    ["ys", "accions", 5555],
];


echo '<table border="1">'; 

echo "<tr>
<th>Juego</th>
<th>Genero</th>
<th>Año</th>
</tr>";

for ($i = 0; $i < count($juegos); $i++) {
    echo "<tr>";
    echo "<td>" . $juegos[$i][0] . "</td>";
    echo "<td>" . $juegos[$i][1] . "</td>";
    echo "<td>" . $juegos[$i][2] . "</td>";
    echo "</tr>";
}



echo "</table>";



echo '<table border="1">'; 

echo "<tr>
<th>Juego</th>
<th>Genero</th>
<th>Año</th>
</tr>";


foreach ($juegos as $guejo) {
echo "<tr>";
echo "<td>" . $guejo[0] . "</td>";
echo "<td>" . $guejo[1] . "</td>";
echo "<td>" . $guejo[2] . "</td>";
echo "</tr>";
}
echo "</table>";
?>
