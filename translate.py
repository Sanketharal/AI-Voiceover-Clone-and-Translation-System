from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def translate_to_hindi(text):
    # Load the model and tokenizer
    model_name = "facebook/nllb-200-distilled-600M"  # You can choose a different NLLB model size
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # For NLLB models, use the forced_bos_token_id for the target language
    src_lang = "eng_Latn"  # English in Latin script
    tgt_lang = "hin_Deva"  # Hindi in Devanagari script
    
    # Tokenize and translate
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    
    # Get the forced BOS token ID for target language
    # Compatible with older PyTorch versions
    if hasattr(tokenizer, "lang_code_to_id"):
        forced_bos_token_id = tokenizer.lang_code_to_id[tgt_lang]
    else:
        # Alternative approach for tokenizers without lang_code_to_id
        forced_bos_token_id = tokenizer.convert_tokens_to_ids(tgt_lang)
    
    # Generate translation
    translated = model.generate(
        **inputs,
        forced_bos_token_id=forced_bos_token_id
    )
    
    # Decode the translation
    hindi_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
    return hindi_text