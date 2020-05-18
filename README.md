# Comic-Criminal
AI and Data Analysis Project for dsml 2019

Super Hero Effectiveness

Αντικείμενο της εργασίας είναι να μελετηθεί η συσχέτιση μεταξύ εγκληματικότητας και εμφάνισης χαρακτηριστικών διάφορων υπερηρώων στις ΗΠΑ. 

1) Αποθήκευση Διαθέσιμης Πληροφορίας στην Κατάλληλη Μορφή
Στο πρώτο βήμα θα κατεβάσετε τα σύνολα δεδομένων: Super Hero Dataset, Complete Super Hero Dataset, Comic-Characters Dataset, και Crime in Context Dataset: https://www.kaggle.com/thec03u5/complete-superhero-dataset?fbclid=IwAR1fukzJpHF4Z94uUeb3ff3MPncW1pQjWUIQjPL34Nt4piCaqlVtAx_XnWo
https://www.kaggle.com/claudiodavi/superhero-set?fbclid=IwAR1_xm9Xk1ln7q94HvVezKW2RbEmq51xZ-yaEG9sUMXPTSZiipreF39k5bc
https://github.com/fivethirtyeight/data/tree/master/comic-characters?fbclid=IwAR1opMxxfRKsmrPqe_gugsFxLvxi8Yg2D_4xMBEQb2JABkQSEsgdMD_WpI0
https://www.kaggle.com/marshallproject/crime-rates
Θα ενοποιηθούν τα τρία σύνολα δεδομένων σχετικά με υπερήρωες σε triplestore (έχουν κάποιες διαφορετικές στήλες, κάποιες όμοιες με διαφορετική μορφή τιμών (πχ height σε centimetre και σε feet)). Θα αναδομηθούν τα δεδομένα, αξιοποιώντας τη σημασιολογία των δεδομένων (πχ οι στήλες Full Name, Alter Ego, Alias μπορούν να ενσωματωθούν σε έναν ρόλο “hasName”)


2) Εμπλουτισμός Δεδομένων και Ανάλυση με Cognitive Services
Στη συνέχεια θα εμπλουτιστεί το σύνολο δεδομένων με τα παρακάτω βήματα:
α) Θα τρέξετε κάποιον αλγόριθμο από τα clouds για Named Entity Recognition στις στήλες σχετικές με περιοχή όπως “Base” και “Place of Birth” και στη στήλη “relatives”. Για παράδειγμα από την τιμή “currently New York City, formerly Asgard, formerly the fleet of Korbinite ships” Θα εξαχθούν “New York City”, “Asgard”, “Korbonite”. 
β) Επιπρόσθετα θα εμπλουτίσετε όλες τις στήλες που αφορούν γεωγραφικές περιοχές με τα γεωγραφικά μήκη και πλάτη των περιοχών (που υπάρχουν) από geoNames. Τέτοιες στήλες είναι οι “place of birth”, “base” καθώς και η “agency juristiction” του Crime in Context Dataset.
γ) Τέλος θα εξαχθούν οι χρονολογίες από τις αντίστοιχες στήλες, όπως η “First Appearance”

Σε αυτήν την φάση η βάση δεδομένων που έχετε κατασκευάσει συνδέει τα σύνολα σχετικά με υπερήρωες με την εγκληματικότητα στην Αμερική, μέσω των χρονικών και γεωγραφικών χαρακτηριστικών τα οποία είναι στην ίδια μορφή. Στο επόμενο βήμα θα γίνει στατιστική ανάλυση των δεδομένων για την εξαγωγή συμπερασμάτων και τον εντοπισμό πιθανών συσχετίσεων.

3) Περαιτέρω Ανάλυση και Παρουσίαση Δεδομένων
Τέλος θα αναλύσετε παραπάνω τα δεδομένα, μελετώντας συσχετίσεις μεταξύ εγκληματικότητας και εμφάνισης ή χαρακτηριστικών διαφόρων υπερηρώων. Θα χρειαστεί πειραματισμός με διαφορετικές μεθόδους που παρέχουν τα cognitive services και με συνδυασμούς χαρακτηριστικών.
Η βάση δεδομένων και τα αποτελέσματα της περαιτέρω ανάλυσης θα παρουσιαστούν σε κάποιο frontend, στο οποίο θα εμφανίζεται χάρτης (των ΗΠΑ ή του κόσμου), και ο χρήστης θα μπορεί να περιηγείται επιλέγοντας χρονολογία, ή αναζητώντας υπερήρωα.







