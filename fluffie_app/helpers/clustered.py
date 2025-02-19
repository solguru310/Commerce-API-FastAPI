skincare_labels = {
    "acne": ['effective for acne', 'acne-preventing', 'acne-prone skin friendly', 'targets bacne', 'clears blackheads', 'targets blind pimples', 'targets whiteheads', 'blackhead minimizing','cystic acne relief','hormonal-acne friendly'],
    "aging": ['anti-aging', 'wrinkle reducing'],
    "sensitivity": ['sting-free', 'eye-irritation free', 'sensitive eye friendly', 'irritation-free', 'eye-area friendly','eyelid friendly'],
    "dryness": ['hydrating', 'moisturizer', 'hydrates dry areas', 'flake-free'],
    "oiliness": ['controls eyelid oil', 'controls oil', 'oil-free'],
    "pigmentation": ['dark spot reduction', 'pigmentation reduction', 'discoloration reducing', 'age spot reduction', 'sun spot reduction'],
    "scarring": ['scar healing', 'acne scar reducing'],
    "texture": ['skin smoothing', 'softens skin','promotes supple skin'],
    "uneven skin tone": ['evens tone', 'reduces blotchiness','complexion enhancing'],
    "dark circles": ['diminishes dark circles', 'undereye depuffing','eye bag reduction','boosts eye appearance','beneficial for under-eyes', 'enhances eyelid appearance'],
    "sun protection": ['sunscreen comptabile', 'UV protection', 'soothes sunburn'],
    "eczema": ['eczema soothing'],
    "milia": ['targets milia'],
    "dermatitis": ['dermatitis soothing'],
    "psoriasis": ['helps psoriasis'],
    "inflammation":['depuffing'],
    "rosacea": ['rosacea-friendly','calms redness'],
    "firming": ['firming and tightening','plumping'],
    "dull skin": ['revitalizing for dull skin', 'brightening','promotes dewy skin', 'promotes clear skin','skin brightening'],
    "keratosis pilaris": ['keratosis pilaris-friendly'],
    "skin health": ['skin protection', 'balancing' , 'skin barrier-friendly','promotes healthy skin cells','skin balancing','promotes healthy skin'],
    "pores": ['pore strip', 'refines pores', 'pore cleansing', 'non-clogging', 'decongesting'],
    "detox": ['detoxifying', 'skin detoxifying'],
    "hormonal issues": [],
    "tanning": ['tanning'],
    "lip care": ['lip hydrating', 'lip softening', 'lip plumping', 'lip smoothing', 'for oily lips', 'lip makeup compatible', 'lip product comptabile', 'for dehydrated lips', 'smooths lip wrinkles','lip-friendly','mature lip-friendly'],
    "hand and nail care": ['hand softening', 'enhances hand appearance', 'moisturizes hands'],
    "cleansing": ['cleansing','double cleanse appropriate', 'deep cleansing','removes eye makeup well','removes sunscreen well','removes tan well', 'removes lip makeup well','removes makeup well','gentle cleanse'],
    "makeup-related": ['refreshes makeup', 'makeup compatible', 'compatible with primers', 'compatible with other products', 'makeup alternative', 'enhances makeup longevity', 'makeup-free','great as a base'],
    "packaging": ['quality packaging', 'good size', 'travel-friendly', 'easy dispense','quality applicator'],
    "product attributes": ['eco-friendly', 'vegan', 'cruelty free', 'natural product', 'chemical-free','pregnancy-safe', 'clean product'],
    "eyelash and eyebrow care": ['promotes brow growth ', 'brow lifting', 'darkens eyebrows', 'boosts brow volume', 'promotes eyebrow growth', 'enhances brow health & appearance', 'lash strengthening', 'boosts lash growth', 'enhances lash health & appearance', 'enhances lash curl','eyelash darkening','promotes eyelash growth'],
    "texture/formula": ['smooth texture', 'gel cleanser', 'soft texture', 'gel formula', 'creamy', 'lotion', 'mist formula', 'thick', 'grainy texture', 'liquid formula', 'rich', 'foamy lather', 'gentle', 'pleasant texture', 'heavy', 'spray form', 'clay product', 'serum', 'quality ingredients', 'eye cream', 'tinted moisturizer', 'exfoliating scrub', 'mask','strong formula','breathable','non-sticky','lightweight','toner','balm'],
    "exfoliation": ['gentle exfoliate','effective exfoliator','effective chemical exfoliator'],
    "coverage/finish": ['natural finish', 'sheer coverage', 'good coverage', 'nice finish', 'gloss finish', 'non-glossy', 'matte finish', 'buildable','sheer finish','invisible finish'],
    "application": ['easy to apply', 'absorbs well','no rinse required' , 'easy to blend', 'fast-drying', 'mess-free', 'beginner-friendly','easy to remove','easy to mix'],
    "skin type": ['for normal skin', 'for combination skin', 'suitable for all skin types', 'for dry skin', 'for sensitive skin','for oily skin', 'for dehydrated skin', 'acne-prone skin friendly'],
    "skin tone": ['suitable for darker skin tones'],
    "age suitability": ['mature skin-friendly', 'teen-skin friendly', 'suitable for all ages','child-friendly'],
    "skin feeling": ['not tight-feeling', 'soothes irritation','nourishing','pleasant feel', 'cooling', 'tingling sensation','refreshing', 'soothes itchiness', 'rejuvenating', 'drying effect', 'no peeling or flaking','calming','not stripping','skin purging', 'non-drying','pleasant feeling'],
    "fragrance/scent": ['pleasant taste', 'fragrance free', 'pleasant scent'],
    "transferability": ['stain-free', 'transfer-resistant', 'white-cast free', 'cake-free', 'no pilling', 'residue-free', 'streak-free','crease-free'],
    "versatility": ['heat-resistant', 'versatile', 'waterproof', 'long-lasting', 'weatherproof','durable'],
    "color": ['good color accuracy','high color payoff'],
    "usage": ['night use','good for long-term use','overnight use', 'summer suitable','small amount of product required', 'suitable for winter use', 'suitable for daily use', 'seasonal use-friendly', 'suitable for morning use','suitable for long-term use'],
    "promoted": ['promoted reviews'],
    "other skin areas": ['chin-area friendly','jaw-area friendly','neck-friendly','chest-area friendly','T-zone targeted'],
    "price and quality": ['good price','high quality'],
    "general effectiveness": ['effectiveness','effective highlighting','rapid results'],
    "unclassified": ['long battery life', 'red light therapy', 'alternatives']
}


clustered_labels = {
    "Acne and Oil Control": skincare_labels["acne"] + skincare_labels["oiliness"],
    "Anti-Aging and Firming": skincare_labels["aging"] + skincare_labels["firming"],
    "Pore and Texture Refinement": skincare_labels["pores"] + skincare_labels["texture"],
    "Skin Tone and Pigmentation": skincare_labels["pigmentation"] + skincare_labels["uneven skin tone"],
    "Sensitivity and Redness": skincare_labels["sensitivity"] + skincare_labels["rosacea"] + skincare_labels["inflammation"],
    "Hydration and Nourishment": skincare_labels["dryness"],
    "Cleansing and Makeup Removal": skincare_labels["cleansing"],
    "Scarring and Healing": skincare_labels["scarring"] + skincare_labels["skin health"],
    "Dullness and Revitalization": skincare_labels["dull skin"],
    "Specific Conditions": skincare_labels["eczema"] + skincare_labels["milia"] + skincare_labels["dermatitis"] + skincare_labels["psoriasis"] + skincare_labels["keratosis pilaris"],
    "Product Characteristics": skincare_labels["product attributes"] + skincare_labels["texture/formula"] + skincare_labels["coverage/finish"] + skincare_labels["application"] + skincare_labels["fragrance/scent"] + skincare_labels["skin feeling"],
    "Sun and Protection": skincare_labels["sun protection"],
    "Lip and Eye Care": skincare_labels["lip care"] + skincare_labels["eyelash and eyebrow care"],
    "Hand and Nail Care": skincare_labels["hand and nail care"],
    "Skin Type and Tone": skincare_labels["skin type"] + skincare_labels["skin tone"],
    "Age Suitability and Feeling": skincare_labels["age suitability"],
    "Versatility and Usage": skincare_labels["versatility"] + skincare_labels["usage"],
    "Color and Finish": skincare_labels["color"] + skincare_labels["transferability"],
    "Value and Effectiveness": skincare_labels["price and quality"] + skincare_labels["general effectiveness"],
    "Other": skincare_labels["other skin areas"] + skincare_labels["unclassified"],
}