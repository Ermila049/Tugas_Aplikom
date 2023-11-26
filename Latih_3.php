<html>
    <body>
        <form method=get>
        Var 1
        <input type="text" name=x><br>
        Var 2
        <input type="text" name=y><br>
        <select name="opsi">                        <!--tag pembuka select, gunakan atribut "name" saja dan atribut "id" dihapus saja-->
            <option value="jumlah">Penjumlahan</option>                 <!--tag option untuk membuat opsi, "value" itu nilai dari opsi dan "Penjumlahan" itu nama dari opsi-->
            <option value="kurang">Pengurangan</option>
            <option value="kali">Perkalian</option>
            <option value="bagi">Pembagian</option>
        </select>                                   <!--tag penutup select-->
        <input type="submit" name="run" value="Jalankan">
        </form>
        <?php
           error_reporting(0);
            $a=$_GET['x'];
            $b=$_GET['y'];
            if ($_GET['opsi']=='jumlah'){                   /*$_GET['opsi']=='jumlah' untuk mengambil inputan "select" yang memiliki name='opsi' dengan "option" yang memiliki value='jumlah'*/
                $jum=$a + $b;
                echo $a." + ".$b." = ".$jum;
            }
            if ($_GET['opsi']=='kurang'){                   /*$_GET['opsi']=='kurang' untuk mengambil inputan "select" yang memiliki name='opsi' dengan "option" yang memiliki value='kurang'*/
                $jum=$a - $b;
                echo $a." - ".$b." = ".$jum;
            }
            if ($_GET['opsi']=='kali'){                     /*$_GET['opsi']=='kali' untuk mengambil inputan "select" yang memiliki name='opsi' dengan "option" yang memiliki value='kali'*/
                $jum=$a * $b;
                echo $a." x ".$b." = ".$jum;
            }
            if ($_GET['opsi']=='bagi'){                     /*$_GET['opsi']=='bagi' untuk mengambil inputan "select" yang memiliki name='opsi' dengan "option" yang memiliki value='bagi'*/
                $jum=$a / $b;
                echo $a." : ".$b." = ".$jum;
            }
        ?>
    </body>
</html>