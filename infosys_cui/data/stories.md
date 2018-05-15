## meet n' greet
* greet
    - utter_greet
    > handle_user_query

## how to publish
> handle_user_query
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
    > handle_user_info

## num courses
> handle_user_info
* inform{"anz_kuerse":"29"}
    - utter_ask_change_freq
    > handle_user_info

## change freq
> handle_user_info
* inform{"change_freq":"wöchentlich"}
    - action_eval_eingabekanal
    > eingabekanal_empfehlung

## recommend kanal
> eingabekanal_empfehlung{"empfohlenes_kanal":"online"}
  - utter_recommend_online
  - utter_ask_aufwand_ok
  > handle_user_info

## recommend kanal
> eingabekanal_empfehlung{"empfohlenes_kanal":"xml"}
  - utter_recommend_xml
  - utter_ask_aufwand_ok
  > handle_user_info

## aufwand ok
> handle_user_info
* inform("aufwand_ok":"ja")
  - utter_acknowledge_affirm
  - action_eval_eingabeverfahren
  - utter_noch_fragen
  > handle_noch_fragen

## aufwand nok
> handle_user_info
* inform("aufwand_ok":"nein")
  - utter_acknowledge_deny
  - action_eval_eingabeverfahren
  > recommend_verfahren

## recommend verfahren
> recommend_verfahren{"empfohlenes_kanal":"xml"}
  - utter_recommend_extern
  - utter_noch_fragen
  > handle_noch_fragen

## recommend verfahren
> recommend_verfahren{"empfohlenes_kanal":"online"}
  - utter_recommend_redaktion
  - utter_noch_fragen
  > handle_noch_fragen

## handle noch fragen
> handle_noch_fragen
* affirm
  - utter_how_help
  > handle_user_query

## handle noch fragen
> handle_noch_fragen
* deny
  - utter_acknowledge_affirm
  - utter_goodbye

## allgemeine hilfe
> handle_user_query
* ask_help
  - utter_inform_help
  > handle_user_query
  
  ## Generated Story -3374585848858322144
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "51"}
    - slot{"anz_kuerse": "51"}
    - utter_ask_change_freq
* inform{"change_freq": "w\u00f6chentlich"}
    - slot{"change_freq": "w\u00f6chentlich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "xml"}
    - utter_recommend_xml
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "ja"}
    - slot{"aufwand_ok": "ja"}
    - utter_acknowledge_affirm
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "selbst_xml"}
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

## Generated Story 6828230246724744411
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "22"}
    - slot{"anz_kuerse": "22"}
    - utter_ask_change_freq
* inform{"change_freq": "monatlich"}
    - slot{"change_freq": "monatlich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "online"}
    - utter_recommend_online
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "ja"}
    - slot{"aufwand_ok": "ja"}
    - utter_acknowledge_affirm
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "selbst_online"}
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

## Generated Story 6828230246724744411
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "40"}
    - slot{"anz_kuerse": "40"}
    - utter_ask_change_freq
* inform{"change_freq": "wöchentlich"}
    - slot{"change_freq": "wöchentlich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "online"}
    - utter_recommend_online
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "ja"}
    - slot{"aufwand_ok": "ja"}
    - utter_acknowledge_affirm
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "selbst_online"}
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye
    
## Generated Story 6828230246724744411
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "19"}
    - slot{"anz_kuerse": "19"}
    - utter_ask_change_freq
* inform{"change_freq": "täglich"}
    - slot{"change_freq": "täglich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "online"}
    - utter_recommend_online
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "ja"}
    - slot{"aufwand_ok": "ja"}
    - utter_acknowledge_affirm
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "selbst_online"}
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

## Generated Story 6828230246724744411
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "30"}
    - slot{"anz_kuerse": "30"}
    - utter_ask_change_freq
* inform{"change_freq": "täglich"}
    - slot{"change_freq": "täglich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "online"}
    - utter_recommend_online
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "ja"}
    - slot{"aufwand_ok": "ja"}
    - utter_acknowledge_affirm
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "selbst_online"}
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye


## low volume aufwand nok
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "20"}
    - slot{"anz_kuerse": "20"}
    - utter_ask_change_freq
* inform{"change_freq": "monatlich"}
    - slot{"change_freq": "monatlich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "online"}
    - utter_recommend_online
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "nein"}
    - slot{"aufwand_ok": "nein"}
    - utter_acknowledge_deny
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "redaktion"}
    - utter_recommend_redaktion
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

## low volume aufwand nok 2
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "5"}
    - slot{"anz_kuerse": "5"}
    - utter_ask_change_freq
* inform{"change_freq": "wöchentlich"}
    - slot{"change_freq": "wöchentlich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "online"}
    - utter_recommend_online
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "nein"}
    - slot{"aufwand_ok": "nein"}
    - utter_acknowledge_deny
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "redaktion"}
    - utter_recommend_redaktion
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

## low volume aufwand nok 2
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "15"}
    - slot{"anz_kuerse": "15"}
    - utter_ask_change_freq
* inform{"change_freq": "täglich"}
    - slot{"change_freq": "täglich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "online"}
    - utter_recommend_online
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "nein"}
    - slot{"aufwand_ok": "nein"}
    - utter_acknowledge_deny
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "redaktion"}
    - utter_recommend_redaktion
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

    
## Generated Story 8542725125810336708
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "100"}
    - slot{"anz_kuerse": "100"}
    - utter_ask_change_freq
* inform{"change_freq": "t\u00e4glich"}
    - slot{"change_freq": "t\u00e4glich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "xml"}
    - utter_recommend_xml
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "ja"}
    - slot{"aufwand_ok": "ja"}
    - utter_acknowledge_affirm
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "selbst_xml"}
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

## Generated Story 8542725125810336708
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "51"}
    - slot{"anz_kuerse": "51"}
    - utter_ask_change_freq
* inform{"change_freq": "t\u00e4glich"}
    - slot{"change_freq": "t\u00e4glich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "xml"}
    - utter_recommend_xml
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "ja"}
    - slot{"aufwand_ok": "ja"}
    - utter_acknowledge_affirm
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "selbst_xml"}
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye


## high volume aufwand nok
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "100"}
    - slot{"anz_kuerse": "100"}
    - utter_ask_change_freq
* inform{"change_freq": "t\u00e4glich"}
    - slot{"change_freq": "t\u00e4glich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "xml"}
    - utter_recommend_xml
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "nein"}
    - slot{"aufwand_ok": "nein"}
    - utter_acknowledge_deny
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "extern_xml"}
    - utter_recommend_extern
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye

## high volume aufwand nok 2
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "76"}
    - slot{"anz_kuerse": "76"}
    - utter_ask_change_freq
* inform{"change_freq": "wöchentlich"}
    - slot{"change_freq": "wöchentlich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "xml"}
    - utter_recommend_xml
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "nein"}
    - slot{"aufwand_ok": "nein"}
    - utter_acknowledge_deny
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "extern_xml"}
    - utter_recommend_extern
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye
    
## high volume aufwand nok 2
* greet
    - utter_greet
* ask_about_publish
    - utter_inform_publish
    - utter_ask_num_courses
* inform{"anz_kuerse": "60"}
    - slot{"anz_kuerse": "60"}
    - utter_ask_change_freq
* inform{"change_freq": "wöchentlich"}
    - slot{"change_freq": "wöchentlich"}
    - action_eval_eingabekanal
    - slot{"empfohlenes_kanal": "xml"}
    - utter_recommend_xml
    - utter_ask_aufwand_ok
* inform{"aufwand_ok": "nein"}
    - slot{"aufwand_ok": "nein"}
    - utter_acknowledge_deny
    - action_eval_eingabeverfahren
    - slot{"empfohlenes_verfahren": "extern_xml"}
    - utter_recommend_extern
    - utter_noch_fragen
* deny
    - utter_acknowledge_affirm
    - utter_goodbye



