# Задачи по биоинформатике.
1. Скачать нуклеотидную последовательность хромосомы Y в fasta формате (версия генома – hg38, ссылка заархивированного [файла](http://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chrY.fa.gz)). 
	- Посчитать количество нуклеотидов (A, C, G и T) на обратной цепи. Вычислить количество U на РНК транскрипте при условии, что chrY полностью транскрибируется.
	- Вырезать последовательность нуклеотидов с 100000 по 100100 позицию.
	- Для предыдущего пункта выдать reverse, reverse-complement, complement последовательности. Для проверки можно испоьзовать [сайт](http://www.bioinformatics.org/sms/rev_comp.html).
	- Вычелить [GC состав](https://en.wikipedia.org/wiki/GC-content) для последовательностей из предыдущего пункта. Насколько отличается %GC.
2. Разбить файл в fasta формате на два файла в fasta формате. Содержание каждого файла соотвествует нуклеотидным последовательностям с именами left или right.  
    Input file in fasta format:  
    \>Name_1_left  
    ATACATCGTACGTTGATCGATGCTAGCTAGGGG  
    \>Name_2_right  
    AAATATATTTATATGATAGATGATGATTTTTC  
    \>Name_1_right  
    AAATTATATATTATAGAGGAGCGCGAGA  
    \>Name_3_left  
    ATACATCGTACGTTGATCGATGCTAGCTAGCCCCCCCC  
    \>Name_3_right  
    AAATATATTTATATGATAGATGATGATTTTT  
    \>Name_2_left  
    AAATTATATATTATAGAGGAGCG  

    Ouput of file 1 in fasta format:  
    \>Name_1_left  
    ATACATCGTACGTTGATCGATGCTAGCTAGGGG  
    \>Name_2_left  
    AAATTATATATTATAGAGGAGCG  
    \>Name_3_left  
    ATACATCGTACGTTGATCGATGCTAGCTAGCCCCCCCC  
  
    Ouput of file 2 in fasta format:  
    \>Name_1_right  
    AAATTATATATTATAGAGGAGCGCGAGA  
    \>Name_2_right  
    AAATATATTTATATGATAGATGATGATTTTTC  
    \>Name_3_right  
    AAATATATTTATATGATAGATGATGATTTTT  
3. Перевести fastq формат в fasta формат. Проделать обратную процедуру приписав качество \*.  
    Input file in fastq format:  
    @Name_1  
    ATACATCGTACGTTGATCGATG  
    \+  
    !!\*CCC%%%%!%%%%!!679CCC  

4. Скачать координаты транскриптов (версия генома hg38, описание [таблицы](https://genome.ucsc.edu/cgi-bin/hgTables), ссылка заархивированного [файла](http://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/knownGene.txt.gz). Объединить пересекающиеся координаты транскриптов с учетом стренда и названия хромосом.  
    Example of input file:  
    chr1   +  10   100  
    chr1   +  15   300  
    chrX   -   66   89  
    chrX   +  50   100  
    chrX   -   10   500  
  
    Output file:  
    chr1   +  10   300     
    chrX   +  50   100  
    chrX   -   10  500  
    **Дополнительно**. Наличие стренда и хромосомы сделать в качестве аргумента python `./program.py input_file output_file arg`. Если вместо arg записать 0, то объединять без учета стренда и хромосомы. Если отсутствует 1, то объединять без учета стренд, но с учетом хромосомы. Если 2, то объединять без учета хромосомы, но с учетом стренда. Если аргумент равен 3, то объединять с учетом стренда и хромосомы.

5. Имеется два списка генов. Найти общий список генов и уникальные списки генов.  
    List1:  
    ABL  
    AKT1  
    AKT2  
    SOX2  
  
    List2:  
    AKT3  
    ABL  
    NANOG  
    AKT2  
    
6. Посчитать количество уникальных генов в списке  
    List of input file:  
    ABL  
    AKT1  
    AKT2  
    SOX2  
    NANOG  
    SOX2  
    AKT2  
    EMX2  
    AKT1  
    AKT3  
    NANOG  
  
    List of output file:  
    ABL - 1  
    AKT1 - 2  
    AKT2 - 2  
    SOX2 - 2  
    NANOG - 2  
    EMX2 - 1  
    AKT3 - 1 

7. Даны две последовательности одинакового размера ATGTAAAATATATATTGCGTCGTGAA и AATTAGGGTATATATTGCGTCGTGTT. Вычислить [расстояние Хэмминга](https://en.wikipedia.org/wiki/Hamming_distance)

# Задачи по алгоритмам и структурам данных (биоинформатика)

1. Проанализировать генную сеть (граф) транскрипционных факторов [TF](https://en.wikipedia.org/wiki/Transcription_factor) [E.coli](https://en.wikipedia.org/wiki/Escherichia_coli). Вершины - TF (= ген, считаем одной сущностью); направленное ребро(дуга) - тип взаимодействия (активация, ингибирование и дуальное действие). Список TF и взаимодействий можно найти [здесь](http://regulondb.ccg.unam.mx/menu/download/datasets/files/network_tf_tf.txt) (1 столбец - TF, 2 столбец - гены, которые регулируют TF, 3 столбец - тип взаимодействия). Для упрощения 2 столбец будем считать TF.
	- Найти максимальный путь с учетом направленности дуги. Название вершины, с которой происходит старт подается программе в качестве аргумента\*\*.
	- Редуцировать сеть, чтобы существовал максимальный [Гамильтонов путь](https://en.wikipedia.org/wiki/Hamiltonian_path)\*\*.
	- Найти все возможные циклы, состоящие из трех вершин с учетом направленности графа, например 1->2->3->1 (верно), 1->2<-3->1 (неверно)\*.
	- Найти максимальный и минимальный путь без учета направленности графа между двумя задаными TF. Название TF подается в качестве аргументов\*.
	- Посчитать количество TF (количество вершин).
	- Найти вершину с максимальным количеством входящих дуг; какую роль выполняет данный TF в клетке?
	- Найти вершину с максимальным количеством выходящих дуг; какую роль выполняет данный TF в клетке?
	- Является ли граф связным? Если нет, то сколько [компонентов связности](https://en.wikipedia.org/wiki/Connected_component_(graph_theory)).
	- (для тех кому мало) Назовите TF регулирующие ген TF GadX? При каких условия происходит активация экспрессии регуляторов гена TF GadX? С какими процессами связан TF GadX?\*.

2. Проанализировать таблицу с транскриптами человека (версия генома hg38, описание [таблицы](https://genome.ucsc.edu/cgi-bin/hgTables), ссылка заархивированного [файла](http://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/knownGene.txt.gz)). На вход программе подается таблица. Результатом является числовое значение и файл в формате "идентификатор транскрипта|название хромосомы|начало интервала|конец интервала".
	- Отсортировать транскрипты по суммарной длине экзонов каждого транскрипта. Назовите транскрипты с максимальной, медиальной и минимальной длиной\*.
	- Вычеслить количество генов с CDS = 0. Что длинее CDS или суммарная длина экзонов\*?
	- Найти суммарную длину интронов для хромосомы 1-22,X и Y без учета стренда. Интроны не должны пересекаться с экзонами\*.






