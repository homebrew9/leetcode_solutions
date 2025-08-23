from typing import List

class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        N = len(phrases)
        seen = set()
        for i in range(N):
            phrase1 = phrases[i]
            arr1 = phrase1.split()
            for j in range(N):
                if j == i:
                    continue
                phrase2 = phrases[j]
                arr2 = phrase2.split()
                if len(arr1) == 1 and len(arr2) == 1:
                    if phrase1 == phrase2:
                        seen.add(phrase1)
                elif arr1[-1] == arr2[0]:
                    if len(arr2) > 1:
                        seen.add(phrase1 + ' ' + ' '.join(arr2[1:]))
                    else:
                        seen.add(phrase1)
        return sorted(seen)

# Main section
for phrases in [
                  ['writing code','code rocks'],
                  ['mission statement','a quick bite to eat','a chip off the old block','chocolate bar','mission impossible','a man on a mission','block party','eat my words','bar of soap'],
                  ['a','b','a'],
                  ['nrop xshcva twecfm twecfm twecfm xshcva twecfm','ggwznmv twecfm nrop nrop nrop xshcva ggwznmv ggwznmv p twecfm nrop xshcva p p','p p nrop ggwznmv twecfm nrop p p','xshcva twecfm ggwznmv twecfm nrop p ggwznmv p twecfm','xshcva'],
                  ['ni kntqfmv thyqxe dh xhnbd thyqxe s','s oqefp kntqfmv l ts nalc dbnt','l zmb ts thyqxe kxi dh ni ovdqvb dbnt s l j nqirao j l','z ovdqvb qoqhnxt kntqfmv xhnbd j l','zjje l s ysvpvc ysvpvc oqefp rhgfzeaz rhgfzeaz zjje nalc jymavm xhnbd j l l nqirao j xhnbd','ts thyqxe nalc xhnbd ysvpvc l trijn qoqhnxt zaowxcc qtp lirhaxd j xhnbd zbvntzo lirhaxd vhyntf z','qtp ovdqvb dh jymavm kntqfmv zjje qtp qoqhnxt zjje zjje qtp j rhgfzeaz ts z j','ysvpvc kxi','nalc zaowxcc kxi','j nqirao vhyntf j j j jymavm rhgfzeaz zjje ts qtp lirhaxd j','ysvpvc dbnt zbvntzo qtp trijn','z nalc qtp qtp ni ts','dh','l lirhaxd dh ysvpvc kntqfmv j zjje ysvpvc ysvpvc trijn s dh dh dbnt dh','vhyntf thyqxe ysvpvc trijn','zbvntzo vhyntf zaowxcc vhyntf ni z qoqhnxt j zmb l ni','kntqfmv ni ovdqvb ni zmb oqefp kntqfmv j l zjje zbvntzo nqirao nqirao s','qtp lirhaxd zbvntzo zjje thyqxe nalc kxi zjje dbnt l z j','z thyqxe oqefp trijn lirhaxd jymavm zjje','zaowxcc zaowxcc zaowxcc thyqxe ni','qoqhnxt lirhaxd zjje vhyntf s','trijn xhnbd l ni kxi j s j trijn ysvpvc nqirao ts kntqfmv qtp vhyntf trijn j dbnt ts nqirao','qtp z qoqhnxt oqefp ts oqefp kntqfmv thyqxe s','zmb ni s nqirao rhgfzeaz nqirao vhyntf rhgfzeaz ovdqvb dbnt vhyntf l l ts','nqirao thyqxe kxi thyqxe l zmb j nqirao zmb ysvpvc zbvntzo l nalc j ni z ts xhnbd z kntqfmv kxi','dbnt qoqhnxt zjje','trijn s','xhnbd ni qtp j qoqhnxt zjje zaowxcc ni ts dh xhnbd zjje z dh ts','vhyntf s ovdqvb oqefp z zbvntzo trijn qoqhnxt oqefp trijn kntqfmv qoqhnxt l zaowxcc ni','l vhyntf trijn dh lirhaxd zmb dbnt vhyntf qoqhnxt ni l j s'],
               ]:
    print(f'phrases  = {phrases}')
    sol = Solution()
    r = sol.beforeAndAfterPuzzles(phrases)
    print(f'r = {r}')
    print('==============================')






























