language_info:
  flag: "🇺🇸"
  code: en

STRINGS:
  notes:
    # /save
    note_saved: "🗒 Note <code>{note_name}</code> saved in <b>{chat_title}</b>!"
    note_updated: "🗒 Note <code>{note_name}</code> updated in <b>{chat_title}</b>!"
    you_can_get_note: "\nYou can retrieve this note by using <code>/get {note_name}</code>, or <code>#{note_name}</code>"
    # Translator note: please keep sure that you don't have space in the end of string
    note_aliases: "\nNote aliases:"
    blank_note: "Saving blank note is not allowed!"
    notename_cant_contain: "Note name can't contain \"<code>{symbol}</code>\"!"

    # /get
    cant_find_note: I can't find this note in <b>{chat_name}</b>!
    no_note: "Can't find that note."
    no_notes_pattern: "No notes found by pattern <code>%s</code>"
    u_mean: "\nDid you mean <code>#{note_name}</code>?"

    # /notes
    notelist_no_notes: "There aren't any notes in <b>{chat_title}</b>!"
    notelist_header: "<b>Notes in {chat_name}</b>:"
    notes_in_private: "Click below button to get notes list."
    notelist_search: |
      <b>Pattern:</b> <code>{request}</code>
      <b>Matched notes:</b>
    # /clear
    note_removed: "Note <code>#{note_name}</code> removed in <b>{chat_name}</b>!"
    note_removed_multiple: |
      Removed multiple notes in <b>{chat_name}</b>
      <b>Removed:</b><code>{removed}</code>
    not_removed_multiple: "<b>Not removed:</b><code>{not_removed}</code>"

    # /clearall
    clear_all_text: "This will remove all notes from {chat_name}. Are you sure?"
    clearall_btn_yes: "Yes. Remove all my notes!"
    clearall_btn_no: "No!"
    clearall_done: "All (<code>{num}</code>) notes in {chat_name} were removed!"

    # /search
    search_header: |
      <b>Search request in {chat_name}</b>:
      <b>Pattern:</b> <code>{request}</code>
      <b>Matched notes:</b>
    # /noteinfo
    note_info_title: "<b>Note info</b>\n"
    note_info_note: "Note names: %s\n"
    note_info_content: "Note content: %s\n"
    note_info_parsing: "Parse mode: <code>%s</code>\n"
    note_info_created: "Was created in: <code>{date}</code> by {user}\n"
    note_info_updated: "Last updated in: <code>{date}</code> by {user}\n"
    user_blocked: "Write /start in my PM!"

    # /privatenotes
    private_notes_false_args: "You have 2 options <code>Disable</code> and <code>Enable</code>!"
    already_enabled: "Private notes are already enabled in %s"
    current_state_info: "Private notes are currently <code>{state}</code> in <b>{chat}</b>!"
    enabled_successfully: "Private notes are <b>Enabled</b> in %s successfully!"
    disabled_successfully: "Private notes are <b>Disabled</b> in %s successfully!"
    not_enabled: "Private notes are not enabled."
    privatenotes_notif: "You have been successfully connected to <b>{chat}</b> notes! To disconnect please use command <code>/disconnect</code>!"
    enabled: 'Enabled'
    disabled: 'Disabled'

    # /cleannotes
    clean_notes_enable: "Cleaning notes successfully enabled in <b>{chat_name}</b>"
    clean_notes_disable: "Cleaning notes successfully disabled in <b>{chat_name}</b>"
    clean_notes_enabled: "Cleaning notes currently is <b>enabled</b> in <b>{chat_name}</b>"
    clean_notes_disabled: "Cleaning notes currently is <b>disabled</b> in <b>{chat_name}</b>"

    # Filter
    filters_title: 'Send a note'
    filters_setup_start: 'Please send a note name.'

    #delmsg_no_arg: "deletemsg button can contain only 'admin' or 'user' argument!"
    #bot_msg: "I'm sorry, I am not able to get this message, probably this a other bot's message, so I can't save it."
  filters:
    no_filters_found: "No filters was found in <b>{chat_name}</b>!"

    # /addfilter
    anon_detected: Being anonymous admin, you cannot add new filters, use connections instead.
    regex_too_slow: "Your regex pattern matches too slowly (more than the half of second) and it can't be added!"
    cancel_btn: "🛑 Cancel"
    adding_filter: |
      Adding filter <code>{handler}</code> in <b>{chat_name}</b>
      Select action below:
    saved: "New filter was successfully saved!"

    # /filters
    list_filters: "Filters in <b>{chat_name}</b>:\n"

    # /delfilter
    no_such_filter: I can't find that filter in <b>{chat_name}</b>, you can check what filters are enabled with the <code>/filters</code> command.
    del_filter: "Filter with handler '<code>{handler}</code>' was successfully removed!"
    select_filter_to_remove: |
      I have found many filters with handler '<code>{handler}</code>'.
      Please select one to remove:
    # /delfilters or /delallfilters
    not_chat_creator: Only chat creators can use this command!
    delall_header: This would delete all filters in this chat. This IS irreversible.
    confirm_yes: ⚠ Delete all
    confirm_no: ❌ Cancel
    delall_success: Successfully deleted all ({count}) filters in this chat!

  warns:
    # /warn
    warn_sofi: "Haha no way to warn myself!"
    warn_self: "Do you wanna warn yourself? Just leave the chat then."
    warn_admin: "Well.. you are wrong. You can't warn an admin."
    warn: "{admin} has warned {user} in <b>{chat_name}</b>\n"
    warn_bun: "Warnings has been exceeded! {user} has been banned!"
    warn_num: "Warns: {curr_warns}/{max_warns}\n"
    warn_rsn: "Reason: <code>{reason}</code>\n"
    max_warn_exceeded: Warnings has been exceeded! {user} has been {action}!
    max_warn_exceeded:tmute: Warnings has been exceeded! {user} has been tmuted for {time}!

    # warn rmv callback
    warn_no_admin_alert: "⚠ You are NOT admin and cannot remove warnings!"
    warn_btn_rmvl_success: "✅ Warning removed by {admin}!"

    # /warns
    warns_header: "Here are your warns in this chat \n\n"
    warns: "{count} : <code>{reason}</code> by {admin}\n"
    no_warns: "Well, {user} doesn't have any warns."

    # /warnlimit
    warn_limit: "Warn limit in <b>{chat_name}</b> is currently: <code>{num}</code>"
    warnlimit_short: 'Warnlimit should be at least 2!'
    warnlimit_long: 'Warnlimit should be shorter than 1 000!'
    warnlimit_updated: '✅ Warnlimit successfully updated to {num}'

    # /delwarns
    purged_warns: "{admin} reset <code>{num}</code> warns of {user} in <b>{chat_title}</b>!"
    usr_no_wrn: "{user} doesn't have any warns to reset."
    rst_wrn_sofi: 'Daisy never had warns to reset.'
    not_digit: Warnlimits should be digits!

    # /warnmode
    same_mode: This is the current mode! How can I change it?
    no_time: For selecting mode 'tmute' you have to mention time!
    invalid_time: Invalid time!
    warnmode_success: Warn mode of <b>%s</b> has successfully changed to <b>%s</b>!
    wrng_args: |
      These are the available options:
    mode_info: |
      Current mode in this chat is <b>%s</b>.
    banned: banned
    muted: muted

    filters_title: Warn the user
    filter_handle_rsn: Automated filter action!

  msg_deleting:
    no_rights_purge: "You don't have enough rights to purge in this group!"
    reply_to_msg: "Reply to a message to delete!"
    purge_error: "I can't continue purge, mostly because you started purge from a message that was sent older than 2 days."
    fast_purge_done: "<b>Fast purge completed!</b>\nThis message will be removed in 5 seconds."
    purge_user_done: "All messages from {user} were successfully deleted!"
  misc:
    your_id: "Your ID: <code>{id}</code>\n"
    chat_id: "Group ID: <code>{id}</code>\n"
    user_id: "{user}'s ID: <code>{id}</code>\n"
    conn_chat_id: "Current connected chat ID: <code>{id}</code>"
    help_btn: "Click me for help!"
    help_txt: "Click the button below for help!"

    delmsg_filter_title: 'Delete the message'
    send_text: Please send the reply message!
    replymsg_filter_title: 'Reply to message'

    send_customised_reason: Send the <i>reason</i> you want to include in action message. "<code>None</code>" for <i>no reason</i> to be given!
    expected_text: Expected a text message!

  promotes:
    promote_success: "{user} was successfully promoted in {chat_name}!"
    promote_title: "\nWith custom role <code>{role}</code>!"
    rank_to_loong: "Custom role text cannot be longer than 16 symbols."
    promote_failed: "Promotion failed! Check if I have rights to."
    demote_success: "{user} was successfully demoted in {chat_name}!"
    demote_not_admin: "That user isn't admin."
    demote_failed: "Demotion failed. Maybe I can't demote or the person is promoted by someone else?"
    cant_get_user: "I couldn't get the user! If you mind, please reply to his message and try again."
    cant_promote_yourself: "You can't promote yourself."
    emoji_not_allowed: "I'm sorry, but admin roles can't have emojis 😞"

  pm_menu:
    start_hi_group: 'Hey there! My name is Miss Nelly'
    start_hi: "Hey there! My name is <b>Miss.</b>\nI can help manage your groups with useful features, feel free to add me to your groups!
    btn_help: "❔ Help"
    btn_lang: "🇺🇸 Language"
    btn_channel: "🙋‍♀️ intimacyfolks"
    btn_group: "👥 intimacyfolkz"
    btn_group_help: "Click me for help!"
    back: "🏃‍♂️ Back"

    # /help
    help_header: "Hi Boss! I'm <b>Miss Nelly</b>. An anime themed super powerful group management bot with many handy tools. So why are you waiting. Let me to assist you"
    click_btn: Click here

  disable:
    #/disableable
    disablable: "<b>Disable-able commands:</b>\n"

    #/disabled
    no_disabled_cmds: No disabled commands in <b>{chat_name}</b>!
    disabled_list: "<b>Disabled commands in {chat_name}:</b>\n"

    #/disable
    wot_to_disable: "What do you want to disable?"
    already_disabled: "This command is already disabled!"
    disabled: "Command <code>{cmd}</code> was disabled in <b>{chat_name}</b>!"

    #/enable
    wot_to_enable: "What do you want to enable?"
    already_enabled: "This command isn't disabled!"
    enabled: "Command <code>{cmd}</code> was enabled in <b>{chat_name}</b>!"

    #/enableall
    not_disabled_anything: "Nothing was disabled in <b>{chat_title}</b>!"
    enable_all_text: "This will enable all commands in the <b>{chat_name}</b>. Are you sure?"
    enable_all_btn_yes: "Yes. Enable all commands!"
    enable_all_btn_no: "No!"
    enable_all_done: "All (<code>{num}</code>) commands were enabled in the <b>{chat_name}</b>!"
  bot_rights:
    change_info: "I don't have rights to change group info, please make me admin with that right."
    edit_messages: "I don't have rights to edit messages!"
    delete_messages: "I don't have rights to delete messages here."
    ban_user: "I don't have rights to ban users, please make me admin with that right."
    pin_messages: "I don't have rights to pin messages, please make me admin with that right."
    add_admins: "I don't have rights to add admins, please make me admin with that right."
  feds:
    # decorators
    need_fed_admin: "You are not an admin in <b>{name}</b> federation"
    need_fed_owner: "You are not an owner of <b>{name}</b> federation"
    cant_get_user: "Sorry, I can't get that user, try using their user ID"

    # /fnew
    fed_name_long: "Federation name can't be longer than 60 symbols!"
    can_only_1_fed: "Users can only create 1 federation, please remove one."
    name_not_avaible: "Federation with name <code>{name}</code> already exits! Please use another name."
    created_fed: |
      Congrats, you have successfully created a federation.
      <b>Name:</b> {name}
      <b>ID:</b> <code>{id}</code>
      <b>Creator:</b> {creator}
      Use <code>/fjoin {id}</code> to connect federation to chat\
    disallow_anon: As an anonymous admin you cannot create new federation!

    # /fjoin
    only_creators: "You must be the chat creator to be able to connect chat to a federation."
    fed_id_invalid: "The given federation ID is invalid! Please give me a valid ID."
    joined_fed_already: "This chat has already joined a federation! Please use /fleave to leave that federation"
    join_fed_success: "Great! Chat <b>{chat}</b> is now a part of <b>{fed}</b> federation!"
    join_chat_fed_log: |
