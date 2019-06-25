from nlglib.realisation.simplenlg.realisation import Realiser
from nlglib.microplanning import *

realise_en = Realiser(host='nlg.kutlak.info', port=40000)
realise_es = Realiser(host='nlg.kutlak.info', port=40001)


def main():
    p = Clause(Mara, perseguir, un mono)
    p['TENSE'] = 'PAST'
    # expected = 'Mara persigue un mono'
    print(realise_es(p))
    p = Clause(NP(la, rpida, corredora), VP(perseguir), NP(un, mono))
    subject = NP(la, corredora)
    objekt = NP(un, mono)
    verb = VP(perseguir)
    subject.premodifiers.append(rpida)
    p.subject = subject
    p.predicate = verb
    p.object = objekt
    # expected = 'La rpida corredora persigue un mono.'
    print(realise_es(p))
    p = Clause(NP('this', 'example'), VP('show', 'how cool simplenlg is'))
    # expected = This example shows how cool simplenlg is.
    print(realise_en(p))


if __name__ == '__main__':
    main()