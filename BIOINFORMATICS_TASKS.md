# Задачи по биоинформатике.
1. Скачать нуклеотидную последовательность хромосомы Y в fasta формате (версия генома – hg38, ссылка заархивированного [файла](http://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/chrY.fa.gz)). Посчитать количество нуклеотидов (A, C, G и T) на обратной цепи.
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
    ABL      chr1   +  15   300  
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
    
# Алгоритмические задачи

1.Проанализировать генную сеть (граф) транскрипционных факторов [TF], https://en.wikipedia.org/wiki/Transcription_factor) [E.coli] (https://en.wikipedia.org/wiki/Escherichia_coli). Вершины (TF = белок = ген), направленное ребро или дуга (тип взаимодействия: активация - зеленого цвета, ингибирование - красного цвета; дуальное действие - коричневого цвета). Если TF регулирует собственный ген, то в зависимости от типа регуляции вершина обозначается соотвествующим цветом, как и дуга. Список TF и взаимодействий можно найти [здесь] http://regulondb.ccg.unam.mx/menu/download/datasets/files/network_tf_tf.txt (1 столбец - TF, 2 столбец - гены, которые регулируют TF, 3 столбец - тип взаимодействия). Для упрощения 2 столбец будем считать TF.
	- найти максимальный Гамильтонов путь с учетом направленности дуги. Название вершины, с которой происходит старт подается программе в качестве аргумента\*\*.
	- найти все возможные циклы, состоящие из трех вершин без учет направленности графа\*.
	- посчитать количество TF (количество вершин)
	- найти вершину с максимальным количеством входящих дуг
	- найти вершину с максимальным количеством выходящих дуг
	- является ли граф связным? Если нет, то сколько [компонентов связности] (https://en.wikipedia.org/wiki/Connected_component_(graph_theory))








