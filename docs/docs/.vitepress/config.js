export default {
    title: 'Self Steering Vehicle',
    description: 'Documentation for the BeCreative self steering car project',
    themeConfig: {
        socialLinks: [
            { icon: 'github', link: 'https://github.com/nagsterFVZ/self-driving' },
          ],
          nav: [
            { text: 'Project', link: '/project/' },
            { text: 'Files', link: '/files/' },
            { text: 'Blogs', link: '/blogs/' },
          ],
        sidebar: {
            '/project/': [
                {
                    text: 'Introduction',
                    items: [
                        { text: 'The Project', link: '/project/' },
                        { text: 'Parts', link: '/project/-' },
                    ]
                },
                {
                    text: 'Research',
                    items: [
                    { text: 'Control System', link: '/project/research/control' },
                    ]
                },
                {
                    text: 'Installation',
                    items: [
                    { text: 'Introduction', link: '/project/-' },
                    { text: 'Research', link: '/project/-' },
                    ]
                },
            ],
            '/files/': [
                {
                    text: 'Vehicle',
                    items: [
                        // { text: 'The Project', link: '/files/' },
                    ]
                },
                {
                    text: 'Schematics',
                    items: [
                        // { text: 'The Project', link: '/files/' },
                    ]
                },
            ],
            '/blogs/': [
                {
                    text: 'Personal Blogs',
                    items: [
                        { text: 'Floris', link: '/blogs/floris' },
                    ]
                },
            ]
        }
    }
}
  