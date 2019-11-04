# this is a quick testing script for romance languages


from cube.io_utils.conll import Dataset

train_list = ['../corpus/ud-treebanks-v2.2/UD_Romanian-RRT/ro_rrt-ud-train.conllu',
              '../corpus/ud-treebanks-v2.2/UD_French-Sequoia/fr_sequoia-ud-train.conllu',
              '../corpus/ud-treebanks-v2.2/UD_French-GSD/fr_gsd-ud-train.conllu',
              '../corpus/ud-treebanks-v2.2/UD_Portuguese-Bosque/pt_bosque-ud-train.conllu',
              '../corpus/ud-treebanks-v2.2/UD_Spanish-AnCora/es_ancora-ud-train.conllu',
              '../corpus/ud-treebanks-v2.2/UD_Catalan-AnCora/ca_ancora-ud-train.conllu',
              '../corpus/ud-treebanks-v2.2/UD_French-Spoken/fr_spoken-ud-train.conllu',
              '../corpus/ud-treebanks-v2.2/UD_Galician-CTG/gl_ctg-ud-train.conllu',
              '../corpus/ud-treebanks-v2.2/UD_Italian-ISDT/it_isdt-ud-train.conllu',
              '../corpus/ud-treebanks-v2.2/UD_Italian-PoSTWITA/it_postwita-ud-train.conllu']

dev_list = ['../corpus/ud-treebanks-v2.2/UD_Romanian-RRT/ro_rrt-ud-dev.conllu',
            '../corpus/ud-treebanks-v2.2/UD_French-Sequoia/fr_sequoia-ud-dev.conllu',
            '../corpus/ud-treebanks-v2.2/UD_French-GSD/fr_gsd-ud-dev.conllu',
            '../corpus/ud-treebanks-v2.2/UD_Portuguese-Bosque/pt_bosque-ud-dev.conllu',
            '../corpus/ud-treebanks-v2.2/UD_Spanish-AnCora/es_ancora-ud-dev.conllu',
            '../corpus/ud-treebanks-v2.2/UD_Catalan-AnCora/ca_ancora-ud-dev.conllu',
            '../corpus/ud-treebanks-v2.2/UD_French-Spoken/fr_spoken-ud-dev.conllu',
            '../corpus/ud-treebanks-v2.2/UD_Galician-CTG/gl_ctg-ud-dev.conllu',
            '../corpus/ud-treebanks-v2.2/UD_Italian-ISDT/it_isdt-ud-dev.conllu',
            '../corpus/ud-treebanks-v2.2/UD_Italian-PoSTWITA/it_postwita-ud-dev.conllu']

trainset = Dataset()
devset = Dataset()
for ii in range(len(train_list)):
    trainset.load_language(train_list[ii], ii)
    devset.load_language(dev_list[ii], ii)

from cube.io_utils.trainers import TaggerTrainer
from cube.io_utils.encodings import Encodings
from cube.generic_networks.taggers import BDRNNTagger
from cube.io_utils.config import TaggerConfig

encodings = Encodings()
encodings.compute(trainset, devset)
config = TaggerConfig()
tagger = BDRNNTagger(config, encodings, num_languages=len(train_list))

trainer = TaggerTrainer(tagger, encodings, 20, trainset, devset)
trainer.start_training('../model-mixed', batch_size=1000)