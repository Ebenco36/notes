module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    'plugin:vue/vue3-essential',
    '@vue/standard'
  ],
  parserOptions: {
    parser: '@babel/eslint-parser'
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    // Disable the rule that requires single quotes for strings
    'quotes': ['off'],
    // Disable the rule that disallows extra semicolons
    'no-extra-semi': ['off'],
    // Allow trailing commas in arrays and objects
    'comma-dangle': ['warn', 'always-multiline'],
    // Add a space before function parentheses
    'space-before-function-paren': 'off',
    // Allow both 4-space and 2-space indentation
    indent: 'off',
    'space-before-function': 'off',
    'semi': 'off',
    'no-unused-vars': 'off',
    'prefer-const': 'off',
    'new-cap': 'off',
  },
  overrides: [
    {
      files: [
        '**/__tests__/*.{j,t}s?(x)',
        '**/tests/unit/**/*.spec.{j,t}s?(x)'
      ],
      env: {
        jest: true
      }
    }
  ]
}
