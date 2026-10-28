# Questions for RC 800 Sectional 4.
# Each question: stem, type, target (key letter), opts = list of [code, text, reason].
# code "K" marks the key; any other code is the trap the distractor is built on.
# The builder puts the key at `target` and the distractors, in order, into the other letters.

Q = []

def q(passage, qtype, target, stem, opts, why, src):
    Q.append(dict(passage=passage, type=qtype, target=target, stem=stem, opts=opts, why=why, src=src))

# ================================================================ PASSAGE 1: self-promising

q("p1", "Main idea", "c",
  "Which of the following best captures the central idea of the passage?",
  [["K", "The sceptic's case against self-promising confuses persons with standpoints, but correcting it exposes a further question about what wrong a defaulter commits.",
    "Paragraph 2 says the argument 'passes silently from the identity of persons to the identity of standpoints'; paragraphs 3 and 4 defend and price that reply; paragraph 5 asks 'what, if anything, the defaulter has done wrong' and ends by doubting 'whether what it distinguishes still deserves the name of a promise'."],
   ["P", "Since only those able to take the promisee's standpoint against inclination are bound by self-promises, such promises bind best the people who least need binding.",
    "This is paragraph 4 alone, the 'price' of the defence. It drops the sceptic's argument, the distinction itself and the open question in paragraph 5."],
   ["R", "Because whoever holds a promise to himself can cancel it at pleasure, such a promise is only a resolution, though it may still be useful to make one.",
    "This is the sceptic's view from paragraph 1 with a concession attached. The author calls the argument 'tidier than it looks' and spends paragraph 2 rebutting it; usefulness comes up in paragraph 5 only as a worry about what the obligation rests on."],
   ["B", "Whether a release from an obligation counts depends on the standpoint from which it is given, though in practice no outsider can tell which standpoint that was.",
    "This lifts paragraph 2's point into a rule about obligations in general and adds paragraph 3's concession, but it drops the passage's subject, promises to oneself, along with the price in paragraph 4 and the open question in paragraph 5."]],
  "The passage moves from the sceptic's argument (para 1) to the author's diagnosis of it (para 2), defends that diagnosis (para 3), concedes its cost (para 4) and then raises the harder question of what a defaulter does wrong (para 5). Only (c) holds both the correction and what it leaves exposed.",
  "Countdown 10 Q75 and Q55 (main idea: a secondary point given the weight of the thesis); AILET 2 Q26 (one strand picked as the whole)")

q("p1", "Weaken (narrow sub-claim)", "a",
  "Which of the following, if true, would most seriously weaken the author's claim in the third paragraph that a person 'can usually tell which question she is asking'?",
  [["K", "Diaries kept as people abandon self-promises show them weighing only their current wishes, yet at that moment most say they are weighing the promise's purpose.",
    "The claim is that a person can tell whether she is asking 'does the purpose still hold?' or 'do I still feel like it?'. If, at the very moment of deciding, people are asking the second while sincerely saying they are asking the first, they cannot tell which question they are asking."],
   ["R", "No one other than the person herself is ever in a position to check whether a release she grants herself was granted as promisee rather than merely as promisor.",
    "This repeats the objection's premise ('no one else can inspect the costume'), which the author already grants. It is about outside checking; the claim under attack is about what the person herself can tell."],
   ["A", "People break a larger share of the promises they make to themselves than of those they make to friends, though they say they feel worse about breaking the latter.",
    "This adds a comparison between self-promises and promises to others that the passage never makes, and break rates say nothing about whether a person can tell which question she is asking."],
   ["T", "People who keep their promises to themselves usually do so out of habit, without first stopping to ask whether the promise's purpose still holds.",
    "This is about why people keep self-promises. The claim under attack is about someone deliberating over a release: whether she can tell which of two questions she is asking."]],
  "The question targets one narrow sub-claim at the end of paragraph 3, not the whole reply. Only (a) is evidence that people misidentify which of the two questions they were asking; the others concern outside checking, a comparison the passage never makes, and habit.",
  "Sectional 1 (weakening a narrow sub-claim: skipped) and the author's-response-to-an-objection miss (an option adding a comparison the author never makes)")

q("p1", "Assumption (challenged)", "d",
  "The author's argument in the second paragraph challenges which of the following assumptions on which the sceptic's argument relies?",
  [["K", "That a person who holds a promise releases it validly whenever she declares it released, in whatever capacity she happens to declare it.",
    "The sceptic moves from 'she holds the promise' to 'she can cancel it at pleasure'. That needs every declaration of release by the holder to count, in whatever role it is made. Paragraph 2 denies exactly this: 'It is settled by asking in which role she decided… Only the second releases.'"],
   ["T", "That a promise gives rise to a genuine claim only where some second party stands ready to complain whenever the promise is broken.",
    "This is the worry of paragraph 5, and the author half-grants it there ('no second party whose complaint survives her indifference'). Paragraph 2 does not challenge it."],
   ["L", "That a release extracted from a promisee who has been worn down, or who was deceived about what the promise protected, is defective.",
    "This is the author's own premise in paragraph 2, not an assumption of the sceptic's, and the author relies on it rather than challenging it."],
   ["R", "That a promise to oneself differs from a resolution only in the dignified vocabulary in which the speaker chooses to express her intention.",
    "This echoes the sceptic's conclusion ('a resolution in borrowed clothes… dignified by a vocabulary'). It is what the argument concludes, not an assumption it relies on."]],
  "An assumption the author challenges must be something the sceptic's reasoning needs and paragraph 2 denies. The sceptic needs the holder's release to be valid at pleasure; paragraph 2 makes validity depend on the role in which she decides.",
  "AILET 5 Q34 (an observation or conclusion picked over the assumption) and Sectional 2 Q22")

q("p1", "Word in context", "b",
  "As used in the first paragraph, the word 'creditor' (in 'a vocabulary that implies a creditor where there is none') most nearly means:",
  [["K", "a party owed the performance, because no second person exists to whom a self-promise could be kept.",
    "The sceptic's point is that self-promising talk implies a second party with a claim, and there is none. Paragraph 5 uses the same idea: 'a claimant whose grievance does not depend on my feelings about it'."],
   ["F", "a lender of money, because the sceptic's argument turns on who holds the power to cancel what is owed.",
    "This is the dictionary sense. The reason echoes the passage, but nothing in it involves money: the missing 'creditor' is whoever is owed the promised performance."],
   ["F", "one who gives credence, because the sceptic calls a self-promise only 'a statement of present intention'.",
    "This takes 'credit' in the sense of belief. The sceptic's complaint is that no one is owed anything, not that no one believes the statement."],
   ["F", "a guarantor of the promise, because Hobbes's sovereign can both bind and release himself whenever he likes.",
    "The reason restates Hobbes accurately, but a guarantor answers for someone else's obligation. The party the sceptic finds missing is the one to whom the performance is owed."]],
  "A 'creditor' is the one to whom something is owed. Here the 'something' is the promised performance, and the sceptic's charge is that self-promising implies such a party where none exists.",
  "Countdown 6 Q14 'immersion' and AILET 5 Q16 'venerable' (dictionary sense over the contextual one)")

q("p1", "Application / analogy", "d",
  "Which of the following is most closely analogous to the distinction the author draws in the second paragraph?",
  [["K", "A referee who is also playing in a friendly match may award a penalty only by judging as a referee would, not because it would help his own side.",
    "One person holds two roles; a decision counts only if it is made in the role that has the authority, not in the role whose interest it suits. That is the structure of 'It is settled by asking in which role she decided.'"],
   ["M", "A committee may overrule its chair only by a majority vote of its members, so that the chair's own wishes cannot settle a disputed question.",
    "Here authority is split between different people. The author's point is about two roles inside one person."],
   ["M", "A shopkeeper who borrows from her own till must record the loan in a ledger, so that an auditor can later confirm that it was repaid.",
    "This makes the safeguard an outside check. The author says the distinction's 'proper home is not the tribunal but deliberation'."],
   ["P", "A runner who has promised his coach to train every day can be released by the coach, but not by deciding for himself that he has trained enough.",
    "This involves two people and a release by the promisee, so it matches only the passing point about releases between persons. It has no one person deciding in two different roles."]],
  "The distinction is between two standpoints held by one person, with validity depending on which standpoint a decision comes from. Only the referee is one person in two roles whose decision counts only from the authorised one.",
  "Countdown 10 Q64 and Sectional 1 Q23 (a case that looks similar but works by a different mechanism)")

q("p1", "Would NOT support", "a",
  "Which of the following situations, if true, would NOT support the reasoning in the fourth paragraph that self-promises bind most reliably those who least need binding, because only they can hold to the promisee's standpoint against inclination?",
  [["K", "Disciplined people keep more of their promises to themselves than procrastinators do, but only because the promises they make are smaller and easier to keep.",
    "The outcome matches (disciplined people keep more self-promises), but the cause is different: easier promises, not a stronger hold on the promisee's standpoint. A case explained by a different mechanism does not support the author's reasoning."],
   ["E", "Procrastinators reminded of a promise's purpose at the moment of temptation break it about as often as those who are not reminded at all.",
    "This supports paragraph 4: for the procrastinator the distinction 'describes what he lacks rather than supplying what he needs', so pointing him to the promisee's standpoint does not help."],
   ["E", "A procrastinator's promises to himself grow more reliable only after he has learned, by quite other means, to resist the pull of the moment.",
    "This supports the last line of paragraph 4: success 'presupposes a strength already there'."],
   ["E", "Those who most often break their promises to themselves are least able to put a promise's purpose above their feelings, though they make no more such promises.",
    "This supports the mechanism: failure goes with a faint promisee's voice."]],
  "The question asks about the reasoning (the 'because'), not only the outcome. (a) reaches the same outcome by another route, so it gives no support to the author's explanation.",
  "Countdown 10 Q64 (mechanism) and Sectional 2 Q18 (a situation that supports picked as the one that doesn't)")

# ================================================================ PASSAGE 2: persisters

q("p2", "Primary purpose", "c",
  "What is the primary purpose of the passage?",
  [["K", "To trace how explanations of why some bacteria survive antibiotics have shifted, and to suggest, with a caveat, that such survival may arise by more than one route.",
    "The passage runs from Bigger's observation, through the dormancy and toxin–antitoxin account and the energy account, to single-cell studies; paragraph 5 says 'persistence' may name 'an outcome rather than a mechanism', then adds 'that conclusion must be held loosely'."],
   ["L", "To show that the retraction of the toxin–antitoxin studies has seriously weakened the case for dormancy as the main explanation of persistence.",
    "Paragraph 3: 'The retractions did not refute dormancy'; they removed evidence for 'a dedicated switch', and paragraph 4 then reports 'a striking confirmation of pre-existing dormancy'. It is also one episode, not the passage's purpose."],
   ["W", "To weigh the dormancy and energy accounts against each other and to conclude, with some reservations, that the energy account better explains the evidence.",
    "The author never ranks the two accounts. The single-cell findings point in different directions, and paragraph 5 resists enlisting them 'on one side or the other'."],
   ["B", "To argue that laboratory studies of bacteria grown in rich medium may reveal little about infections, leaving the clinical value of persister research open.",
    "The caveat about rich medium is one qualification in paragraph 5, made about these observations. The passage is not mainly about laboratory studies in general, and it never questions the value of persister research."]],
  "The passage is a history of explanations that ends in a qualified suggestion (several routes to one outcome) and a caveat about laboratory conditions.",
  "Countdown 10 Q75 (a ranking the passage never makes) and AILET 2 Q38 (an unearned absolute)")

q("p2", "Strengthen", "b",
  "Which of the following, if true, would most strengthen the account described in the third paragraph against the toxin–antitoxin account?",
  [["K", "Cells engineered so that none of their antitoxins can be degraded still form persisters at the usual rate, with survival going to those lowest in ATP.",
    "On the toxin–antitoxin account a cell shuts down when 'a chance dip in its supply could free the toxin'. If no antitoxin can be degraded, that route is closed, yet persistence is unchanged and tracks low ATP. That favours the energy account over the programme."],
   ["N", "In many bacterial species, the cells that survive an antibiotic turn out to have been metabolically quiet, rather than active, when the drug first arrived.",
    "Paragraph 3: 'both predict that survivors will be metabolically quiet'. Evidence both accounts predict cannot favour one."],
   ["N", "A culture's average ATP level falls in the minutes before its killing curve flattens, while its toxin–antitoxin activity stays the same throughout.",
    "This mentions both accounts but rests on culture averages, which paragraph 3 calls 'close to useless': a shift 'could reflect a small change in every cell or a large change in a handful'."],
   ["L", "Deleting the toxin–antitoxin modules from a strain that has been checked and found free of phage sharply reduces the rate at which it forms persisters.",
    "This is the clean version of the retracted result, so it supports the toxin–antitoxin account, the opposite of what is asked."]],
  "To favour one account over the other, evidence must be something one predicts and the other does not. Quietness and average ATP fit both; only (b) closes the toxin–antitoxin route and leaves the energy account standing.",
  "Countdown 5 Q69 (generic support picked over the evidence that discriminates) and Sectional 1 Q11")

q("p2", "Assumption", "a",
  "Bigger's conclusion that the surviving cells were not resistant, as the first paragraph reports it, depends on which of the following assumptions?",
  [["K", "Had the survivors been resistant, their descendants would have inherited that resistance and survived the drug better.",
    "Bigger's test was to regrow the survivors and expose their descendants. The descendants 'died as the original had', so the protection 'had not been inherited'. That shows the cells were not resistant only if resistance would have been passed on. If it would not, the test proves nothing."],
   ["A", "The surviving cells had already been dormant when the penicillin arrived, and so offered the drug nothing that it could corrupt.",
    "This is a later explanation of why persisters survive (paragraph 2). Bigger's conclusion that they were not resistant does not depend on it."],
   ["N", "Penicillin kills a bacterium only while the cell is building its wall, so the dividing cells are the ones most exposed to the drug.",
    "This may be true, but the regrowth test does not rely on how penicillin kills."],
   ["N", "Bigger had screened the original culture for resistant cells, and found none, before he first added any penicillin to it.",
    "The conclusion rests on the regrowth test, not on any earlier screening. The passage mentions none, and the conclusion would stand without it, because resistant survivors would have shown up when he regrew them."]],
  "Negate (a): if resistance need not show up in the descendants, then descendants dying 'as the original had' no longer rules out resistance. So the conclusion depends on (a), and needs nothing about how the culture was prepared.",
  "AILET 5 Q34 (a related fact picked over the needed premise) and Sectional 2 Q22")

q("p2", "Detail: why", "c",
  "According to the passage, why did the retractions described in the second paragraph not refute the dormancy explanation of persistence?",
  [["K", "The retracted work concerned what might switch cells off, not whether survivors are quiet, and losing evidence for a switch is no case against dormancy.",
    "Paragraph 3: the retractions 'removed the strongest evidence for a dedicated switch'. The toxin–antitoxin modules were offered as the cause of dormancy (para 2). Removing support for one cause leaves dormancy itself untouched, and the rival account still has survivors 'metabolically quiet'."],
   ["A", "The bacteriophage that contaminated the engineered strains was itself later found to make cells dormant, so dormancy still explained the survival observed.",
    "The passage says only that the phage's presence 'could account for the difference'. It never says the phage made cells dormant."],
   ["L", "The single-cell study had already confirmed pre-existing dormancy in strains that form persisters at the ordinary rate, so dormancy stood regardless of them.",
    "The 2004 study used 'mutant strains that form persisters at many times the ordinary rate', not strains at the ordinary rate."],
   ["X", "Every later study of persistence has confirmed that the survivors are dormant, so losing one line of evidence could not weaken that case.",
    "Paragraph 4 reports a later study whose survivors 'had been growing and dividing much like their neighbours'. Not every study confirms dormancy."]],
  "The passage never states the reason in one sentence. It has to be put together: the modules were one proposed cause of dormancy (para 2), and the retractions removed evidence for that cause, not for dormancy (para 3).",
  "Countdown 9 Q56 (a fact attached to the wrong conclusion) and Countdown 9 Q65 (a general paraphrase over the stated reason)")

q("p2", "Information EXCEPT", "d",
  "The passage provides information to answer each of the following questions EXCEPT:",
  [["K", "How did the phage's presence in the engineered strains account for the difference in persistence?",
    "The phage is mentioned, and paragraph 2 says its presence 'could account for the difference', but the passage never says how. Mentioned is not answered."],
   ["E", "How did Bigger establish that the cells surviving penicillin were not resistant to the drug?",
    "Answered in paragraph 1: he regrew the survivors and found their descendants 'died as the original had'."],
   ["E", "Why does a cell that has stopped growing escape being killed by most bactericidal antibiotics?",
    "Answered in paragraph 2: such drugs corrupt 'a process the cell is actively running', so a stopped cell 'offers the drug nothing to corrupt'."],
   ["E", "What distinguished the mycobacteria that survived isoniazid from their neighbours that were killed?",
    "Answered in paragraph 4: 'the fluctuating level of an enzyme the drug needs to become active'."]],
  "Three questions are answered in the text. The phage question is only raised: the passage says the phage could explain the result, not how.",
  "Sectional 1 Q12 (information-EXCEPT: you treated 'mentioned' as 'answered') and Countdown 9 Q75")

q("p2", "Quoted-line inference", "b",
  "Read the following line from the passage:\n\"Resistance shifts the whole curve; persistence bends its tail.\"\nWhich of the following can be most reasonably inferred from the quoted line?",
  [["K", "If a culture's early decline is unchanged but a small remnant then outlasts far longer exposures, the pattern points to persistence, not resistance.",
    "Persistence leaves the 'steep initial decline' alone and changes only the 'plateau in which a minority outlasts exposures many times longer'. A curve whose early part is unchanged and whose tail lengthens is therefore persistence, not resistance."],
   ["L", "Since persistence affects only the tail, a culture rich in persisters loses the bulk of its cells more slowly at first than an ordinary culture does.",
    "If persistence 'bends its tail', the early decline is untouched. A slower decline from the start would be a shift of the whole curve, which is the mark of resistance."],
   ["X", "Persisters can be recognised only after most of a culture has died, since they show up solely in the far tail of its killing curve.",
    "The line is about the shape of the curve, not the only way to detect persisters. Paragraph 4 describes survivors being watched before 'the drug arrived'."],
   ["A", "Cultures whose killing curves show the steepest initial decline are the ones most likely to contain a surviving minority of persister cells.",
    "This adds a link between the steepness of the decline and the number of persisters, which the passage never draws."]],
  "Resistance moves the whole curve (the drug kills everyone less well); persistence changes only the tail (a minority lasts longer). So a curve with an unchanged steep start and a longer tail indicates persistence.",
  "AILET 2 Q38 (an absolute in an inference option) and Sectional 2 Q16")

# ================================================================ PASSAGE 3: railways of the Raj

q("p3", "Main idea", "d",
  "Which of the following best captures the central idea of the passage?",
  [["K", "Estimates showing that the railways raised incomes answer a different question from the nationalists', and so settle less of the old debate than is commonly supposed.",
    "Paragraph 2 reports the gains; paragraph 3 says the two literatures 'measure the railways against different alternatives' and that an average does not 'settle who received it'; paragraph 4 narrows the famine result; paragraph 5 leaves the financing terms as the charge on which the econometrics 'are silent'."],
   ["P", "Connecting a district to the railway made a failure of its rains much less likely to become famine, since grain could then be brought in from elsewhere.",
    "This is one finding from paragraphs 2 and 4, and it drops the half of paragraph 4 that matters to the author: grain 'could flow out' too."],
   ["R", "Recent econometric work has refuted the nationalist critique of the railways, though the guarantee that financed them was admittedly a poor bargain for India.",
    "Treating the findings as 'a verdict against the nationalists' is the reading the author calls 'tempting' and then resists. And the author says whether the guarantee cost India more is a question on which the evidence is 'silent', not a settled bad bargain."],
   ["B", "Quantitative history can settle a controversy only when its practitioners and their critics have first agreed on what the past is to be compared with.",
    "The point about counterfactuals is made about this one debate. Turned into a rule for all quantitative history, it goes beyond the passage, and it leaves out the railways altogether."]],
  "The passage accepts the econometric gains, then argues that they are measured against a different alternative from the critics' and so settle only part of the dispute: outright impoverishment, not alternatives, distribution or the guarantee. (d) has both halves.",
  "Countdown 10 Q75 and Q55 (main idea: a part, or the view the author resists, picked as the whole)")

q("p3", "Weaken", "a",
  "Which of the following, if true, would most weaken the conclusion Donaldson drew from the lines that were approved but never built?",
  [["K", "Most approved lines that were never built had been dropped because surveys judged the districts they would serve poor and unpromising.",
    "The phantom routes are a control: if planners picked growing places, those districts should have grown too. If the unbuilt lines were dropped precisely because their districts looked poor, they were not like the built ones, and their lack of growth no longer shows that the railway caused the gains elsewhere."],
   ["L", "Before any lines were planned, districts along the phantom routes had grown at much the same rate as the districts that the railway later reached.",
    "This makes the two groups more comparable, so it strengthens the control rather than weakening it."],
   ["R", "Nationalist critics complained that the lines were laid to carry raw cotton to the ports rather than to serve the districts they crossed.",
    "This repeats paragraph 1. It concerns the purpose of the lines, not whether the unbuilt lines are a fair control."],
   ["T", "In connected districts, grain merchants' incomes rose quickly while the real wages of the labourers who worked the land barely moved.",
    "This bears on who gained (paragraph 3), not on whether the railway caused the average gain. The author notes that an average can rise while the labourer 'gains little'."]],
  "The inference works only if the unbuilt lines are a fair comparison. (a) shows they were selected for being unpromising, so the comparison fails.",
  "Sectional 1 (challenging a paragraph's conclusion: an echo that hits a different target) and Countdown 5 Q76")

q("p3", "Conclusion (two paragraphs)", "c",
  "Which of the following conclusions is best supported by the third and fourth paragraphs taken together?",
  [["K", "Both findings are averages, and neither rules out particular people or districts having lost out even as the average improved.",
    "Paragraph 3: an average gain does not 'settle who received it', since the labourer may gain 'little'. Paragraph 4: the famine finding 'measures how far the link… weakened on average, not whether particular districts in particular years were stripped of food'. The same limit applies to both."],
   ["L", "Unlike the income finding, the famine finding measures the railways against an India in which no district had yet been connected at all.",
    "Both findings compare connected districts with unconnected ones, and the passage draws no such contrast between them. What the two paragraphs share is a point about averages, not about the comparison."],
   ["A", "The famine finding is more trustworthy than the income finding, since it rests on records of rainfall rather than on estimates of output.",
    "The author never ranks the two findings or questions the data behind either."],
   ["R", "Both findings show that the nationalist critics were wrong about the railways, though each of them shows it for a different reason.",
    "This is the reading paragraph 3 calls 'tempting' and then resists; paragraph 4 adds that 'the agreement is narrower than it looks'."]],
  "Paragraphs 3 and 4 make the same move twice: an average gain, whether in income or in protection from famine, can coexist with losses for particular people or places.",
  "Sectional 1 Q4 and Countdown 9 Q76 (a conclusion that needs two paragraphs, against one that repeats a view the author reports)")

q("p3", "Figure of speech", "c",
  "Which of the following figures of speech is most prominently employed in the line below?\n\"The verdict and the indictment pass each other like trains on parallel tracks, each keeping to its own timetable and neither arriving at the other's station.\"",
  [["K", "Simile, because the comparison of the two bodies of work with trains is made explicit with 'like' and then drawn out through 'timetable' and 'station'.",
    "The comparison is announced with 'like', and the rest of the sentence extends the image. An explicit comparison with 'like' or 'as' is a simile, however far it is extended."],
   ["F", "Metaphor, because the verdict and the indictment are pictured as trains, an image the author carries on through 'timetable' and 'station'.",
    "The clause describes the image correctly, but the comparison is explicit ('like trains'), so the figure is a simile. A metaphor would say the verdict and the indictment are trains."],
   ["F", "Personification, because two bodies of scholarship are made to keep their own 'timetable' and miss each other's 'station', as if they had purposes.",
    "Travelling, keeping a timetable and arriving at a station are what trains do, not what persons do. The arguments are given a train's properties, not human ones."],
   ["F", "Analogy, because the author argues from how railway timetables are drawn up to how historians ought to choose the comparisons they make.",
    "Nothing is said about how timetables are drawn up, and no argument runs from railways to historical method. The line is one image, not reasoning from a parallel case."]],
  "'Like trains on parallel tracks' is an explicit comparison, so the figure is a simile, extended through 'timetable' and 'station'. The metaphor option describes the image accurately; only its label is wrong. In Sectional 3 the key was a metaphor; here 'like' does the work.",
  "Countdown 6 Q7 (simile, metaphor and analogy confused) and Sectional 3 (metaphor against analogy)")

q("p3", "Function of a detail", "b",
  "The author sets out the nationalists' charges in the first paragraph in some detail primarily in order to",
  [["K", "prepare for the later argument that the econometrics refute the claim of outright loss and leave the other charges open.",
    "The detail pays off on a second reading: the ports and irrigation return in paragraph 3 ('canals, or lines laid to serve inland markets rather than the ports'), the guarantee in paragraph 5, while 'impoverished India outright' is the one point on which 'the evidence has moved decisively against it'."],
   ["A", "show how much of the nationalist case depended on claims the critics had no means of testing with the data of their day.",
    "Paragraph 2 notes the question was reopened 'with tools the nationalists did not possess', but the detail of paragraph 1 is not there to show what the critics could test. It sets up the later sorting of their charges."],
   ["R", "present the nationalist view that the author then goes on to defend, against the econometric findings, in the rest of the passage.",
    "The author does not defend the original case: 'None of this rescues the nationalist case in its original form'."],
   ["A", "establish that the guarantee system, rather than the railways themselves, was the chief cause of the poverty of colonial India.",
    "The author never ranks the causes of poverty, and says whether the guarantee cost India more than the railways gave back cannot be settled from this evidence."]],
  "Each charge in paragraph 1 is picked up later and sorted into the one the evidence refutes and the ones it leaves open.",
  "AILET 5 Q6 (effect of a detail) and Countdown 6 Q13 (a local point taken for the main one)")

q("p3", "Word in context", "a",
  "As used at the end of the first paragraph, the word 'charge' (in 'less an investment in India than a charge levied on it') most nearly means:",
  [["K", "a cost imposed, because the critics held that India paid for lines whose gains went largely to others.",
    "'Levied' and the contrast with 'investment' fix the sense: a financial burden placed on India, not an outlay that would repay it."],
   ["R", "an accusation, because the paragraph opens with the 'charge against the railways' that the nationalists pressed.",
    "The clause is true: that is the sense of 'charge' in the paragraph's first sentence. But at the end the word is 'levied' and set against 'investment', which an accusation is not."],
   ["F", "a judge's instruction to a jury, because the paragraph presents the nationalists' case as an indictment.",
    "The paragraph does use the language of indictment, but nothing is being instructed. 'Levied on it' names a burden imposed on India."],
   ["F", "a responsibility entrusted, because the lines were placed in the charge of the British companies that built them.",
    "The clause is true to the passage (the lines were 'built by British companies'), but that is the sense of 'in the charge of'. A responsibility is not 'levied on' anyone."]],
  "The paragraph uses 'charge' twice in two senses. Every reason clause here is true to the passage; only 'levied' and the contrast with 'investment' decide the sense at the end.",
  "Countdown 6 Q14 'immersion' and AILET 5 Q16 'venerable' (the wrong sense of a word the passage uses more than one way)")

# ================================================================ PASSAGE 4: copy-text

q("p4", "Central concern", "b",
  "Which of the following best captures the central concern of the passage?",
  [["K", "Each main way of choosing a revised work's text carries a cost its advocates overlook, and some works may not admit of one authoritative text at all.",
    "Paragraphs 2 and 3 find a value claim 'smuggled' into final intention; paragraph 4 finds the social theory 'pays for the correction'; paragraph 5 finds that the digital promise 'hides' the handing of judgment to the reader, then suggests some works were 'never finished'."],
   ["P", "James's late revisions read his early novels rather than completing them, and whether editors should print the first texts may never be settled.",
    "James is the opening case, not the subject. This leaves out the social theory, digital editions and the closing point about unfinished works."],
   ["W", "The social theory of texts corrects the naivety of the final-intention doctrine and should replace it, though digital editions may yet make the choice unnecessary.",
    "This ranks the social theory above final intention; the author says it 'pays for the correction by dissolving a distinction readers have every reason to keep'. And paragraph 5 denies that digital editions remove the need to choose."],
   ["B", "Attempts to fix the text of a literary work tend to rest on hidden judgments of literary value that editors are usually unwilling to admit openly.",
    "The 'smuggled' value claim is a charge against one doctrine (para 3). The social theory and digital editions are criticised on other grounds, so even hedged this generalises one paragraph to all editing."]],
  "The passage examines three answers to 'which text?' and finds each wanting for a different reason, then suggests the question may sometimes have no answer.",
  "Countdown 10 Q55 and Q75 (main idea: part of the passage, or a ranking it never makes)")

q("p4", "Strengthen", "d",
  "Which of the following, if true, would most strengthen the author's objection to the social theory of texts in the fourth paragraph?",
  [["K", "Critics' readings of particular passages in James have repeatedly changed once a puzzling word was traced to a compositor, not to James.",
    "The objection is that the social theory makes 'whether James wrote a given word' no longer the editor's concern, although readers 'have every reason to keep' that distinction. If interpretations change when a word turns out to be a compositor's, the distinction plainly matters to readers."],
   ["T", "Printers in James's day routinely imposed their own house style on the spelling and punctuation of the novels they set, whatever the author preferred.",
    "This supports Greg's reason for taking accidentals from the earliest version (para 2), or the social theory's picture of many hands. It does nothing for the objection."],
   ["N", "McGann's critique was widely adopted by editors of nineteenth-century fiction in the decades that followed, as older methods fell away.",
    "How widely the critique was adopted says nothing about whether its cost is real."],
   ["N", "Most readers who meet The Portrait of a Lady today first read it in the revised text of 1908, not in the text as first published in 1881.",
    "Which text readers happen to meet says nothing about whether the difference between the author's word and a compositor's matters to them."]],
  "The objection rests on readers' interest in who wrote a word. (d) shows that interest doing real work in reading.",
  "Countdown 5 Q76 (a fact that bears on a different claim) and Countdown 5 Q69")

q("p4", "Assumption", "a",
  "The author's charge in the third paragraph, that the final-intention principle smuggles 'a claim about literary value' into 'a rule about documents', assumes that",
  [["K", "a rule for choosing between texts ought not to rest on a judgment of literary merit that it never states.",
    "'Smuggled' is a criticism only if hiding a value judgment inside a documentary rule is a fault. Negate it (a rule may quietly rest on such a judgment) and the charge loses its force."],
   ["A", "the 1881 text of The Portrait of a Lady is a better novel than the text that James produced for the collected edition.",
    "The author need not prefer either text. The charge is that the principle assumes the last word is best, not that it is worst."],
   ["N", "W. W. Greg would not himself have accepted the principle into which his successors later hardened his own method.",
    "Paragraph 2 says Greg's essay was 'more modest than the uses later made of it', but the charge in paragraph 3 does not depend on what Greg would have accepted."],
   ["N", "Greg's distinction between substantive readings and accidentals cannot be applied to revisions as extensive as James's.",
    "Paragraph 3 says nothing about whether Greg's distinction can be applied. The charge does not depend on it."]],
  "To call a claim 'smuggled' is to object to its being hidden. The author's charge needs the premise that an editorial rule should not rest on an unstated value judgment; it needs no view on which James is better.",
  "AILET 5 Q34 and Sectional 2 Q22 (the assumption, not a claim the author need not hold)")

q("p4", "Grammar", "c",
  "Choose the option that best replaces the words in brackets to make the sentence grammatically correct without changing its meaning.\n\"James rewrote several of his early novels for the collected edition [, it left] readers with two texts to choose between.\"",
  [["K", ", thereby leaving",
    "'Thereby' + -ing attaches the result to the main clause: James rewrote the novels, and the result was two texts."],
   ["G", ", thereby it left",
    "This still joins two independent clauses ('James rewrote…' and 'it left…') with only a comma. 'Thereby' is an adverb, not a conjunction, so it does not cure the comma splice."],
   ["G", "so as to leave",
    "This is grammatical but turns the result into James's purpose, which changes the meaning."],
   ["G", "; thereby leaving",
    "A semicolon must be followed by a full clause. 'Thereby leaving readers…' has no subject or finite verb."]],
  "The original is a comma splice (', it left'). The fix must express a result without a second subject. ', thereby leaving' does; the semicolon version has no clause after the semicolon, ', thereby it left' is still a comma splice, and 'so as to leave' changes result into purpose.",
  "Countdown 10 Q69 and Q74 (grammar: comma splice, 'thereby + -ing', infinitive of purpose)")

q("p4", "Tone", "d",
  "Which of the following best describes the tone of the passage?",
  [["K", "Exacting and even-handed, because it separates Greg from his successors and grants the social theory and digital editions their real merits.",
    "The author distinguishes Greg ('more modest than the uses later made of it') from the hardened principle, says the social theory 'corrects a real naivety' and that the digital 'promise is genuine', and is exacting about what each costs ('smuggled', 'pays for the correction', 'so is what it hides')."],
   ["O", "Detached and analytical, because it sets out the rival editorial doctrines in turn, explaining how each arose and what it claims.",
    "The clause is true, but the label is not: the author judges each doctrine ('smuggled', 'pays for the correction', 'what it hides')."],
   ["O", "Sceptical and wistful, because it ends by suggesting that for some works no single text, and no display of all of them, can be the work.",
    "The clause is true and 'sceptical' fits, but nothing in the passage longs for a lost certainty, so 'wistful' is unsupported."],
   ["O", "Impatient and dismissive, because it finds fault in turn with the final-intention principle, the social theory and the digital promise.",
    "The author does find fault with each, but grants each its due ('more modest', 'corrects a real naivety', 'genuine'). Nothing is impatient or dismissive."]],
  "Every reason clause is true; the labels decide. The author is demanding about every position yet gives each its due, Greg included: exacting and even-handed.",
  "Countdown 5 Q75 ('detached and analytical' picked for a critical passage) and Sectional 1 (a right word paired with an unsupported second word)")

q("p4", "Inference (last paragraph)", "b",
  "Which of the following can be most reasonably inferred from the last paragraph of the passage?",
  [["K", "A digital edition that told its readers which version to read first would, to that extent, be keeping the editor's judgment in place rather than abolishing it.",
    "The paragraph says a reader given every text 'with no guidance on which to read first' has not been freed from the editor's judgment 'so much as handed it'. Guidance on which text comes first is that judgment, so an edition that gives it has kept the editor's role rather than ended it."],
   ["B", "Works that their authors revised more than once were probably, for those authors, never truly finished, however settled their printed text.",
    "The paragraph says only that 'some works' 'may' record this. Extending it to every work revised more than once, even with 'probably', is a generalisation the paragraph does not make."],
   ["A", "Digital editions are less honest than printed ones, since they hide the editor's own choices behind an apparently neutral display of every version.",
    "This adds a comparison with printed editions that the paragraph never makes. What the digital promise hides is that the judgment passes to the reader, not any choice of the editor's."],
   ["R", "A book its author could not leave alone records his final intention more faithfully than any single version of it, however carefully edited, can.",
    "This reuses 'intention, final or otherwise' and reverses it. The paragraph says such revisions may record 'less an intention… than the fact that… the book was never finished'."]],
  "The inference runs from 'no guidance on which to read first… handed it': deciding which text comes first is the editor's judgment, whoever exercises it. An edition that guides the reader has not abolished that judgment.",
  "AILET 2 Q38 (an unearned generalisation, here hedged) and the author's-response miss (an added comparison)")

