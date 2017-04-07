/*************************************************
 * Copyright (c) 2016 Ansible, Inc.
 *
 * All Rights Reserved
 *************************************************/

export default ['i18n', function(i18n) {
    return {
        showHeader: false,
        name: 'configuration_misc_template',
        showActions: true,

        fields: {
            TOWER_URL_BASE: {
                type: 'text',
                reset: 'TOWER_URL_BASE',
            },
            TOWER_ADMIN_ALERTS: {
                type: 'toggleSwitch',
            },
            ORG_ADMINS_CAN_SEE_ALL_USERS: {
                type: 'toggleSwitch',
            }
        },

        buttons: {
            reset: {
                ngClick: 'vm.resetAllConfirm()',
                label: i18n._('Revert all to default'),
                class: 'Form-resetAll'
            },
            cancel: {
                ngClick: 'vm.formCancel()',
            },
            save: {
                ngClick: 'vm.formSave()',
                ngDisabled: true
            }
        }
    };
}
];